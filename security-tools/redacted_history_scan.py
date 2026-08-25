#!/usr/bin/env python3
"""Offline secret/history scanner that never emits matched material or paths."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

MAX_BLOB_BYTES = 2 * 1024 * 1024


@dataclass(frozen=True)
class Pattern:
    name: str
    expression: re.Pattern[bytes]
    severity: str


PATTERNS = (
    Pattern("github-bearer", re.compile(rb"(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})"), "confirmed"),
    Pattern("credential-url", re.compile(rb"https?://[^\s/:]+:[^\s/@]+@(?:github\.com|api\.github\.com)"), "confirmed"),
    Pattern("private-key", re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"), "confirmed"),
    Pattern("aws-access-id", re.compile(rb"(?:AKIA|ASIA)[0-9A-Z]{16}"), "confirmed"),
    Pattern("credential-assignment", re.compile(rb"(?i)(?:password|passwd|secret|api[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9+/=_\-.]{16,}"), "possible"),
    Pattern("local-user-path", re.compile(rb"(?i)(?:[A-Z]:\\Users\\|/home/)[^\s/\\]+"), "possible"),
)

GITHUB_LOCATOR = re.compile(
    rb"(?:https?://)?github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+",
    re.IGNORECASE,
)
# Truncated irreversible aliases; the underlying private locator is never
# committed to the public repository.
FORBIDDEN_LOCATOR_ALIASES = {"EVD-2dcb3dddc1ce1dd3"}


def run_git(*args: str) -> bytes:
    return subprocess.run(
        ["git", *args], check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
    ).stdout


def alias_for(category: str, matched: bytes) -> str:
    digest = hashlib.sha256(category.encode("utf-8") + b"\0" + matched).hexdigest()
    return "EVD-" + digest[:16]


def scan_bytes(
    data: bytes,
    public_boundary: bool = False,
    forbidden_locator_aliases: set[str] | None = None,
) -> list[dict[str, str]]:
    if b"\0" in data:
        return []
    findings: list[dict[str, str]] = []
    for pattern in PATTERNS:
        for match in pattern.expression.finditer(data):
            findings.append(
                {
                    "category": pattern.name,
                    "severity": pattern.severity,
                    "alias": alias_for(pattern.name, match.group(0)),
                }
            )
    if public_boundary:
        forbidden = (
            FORBIDDEN_LOCATOR_ALIASES
            if forbidden_locator_aliases is None
            else forbidden_locator_aliases
        )
        for match in GITHUB_LOCATOR.finditer(data):
            normalized = re.sub(rb"^https?://", b"", match.group(0).lower())
            locator_alias = alias_for("private-locator", normalized)
            if locator_alias in forbidden:
                findings.append(
                    {
                        "category": "private-locator",
                        "severity": "confirmed",
                        "alias": locator_alias,
                    }
                )
    return findings


def current_blobs() -> dict[str, str]:
    entries = run_git("ls-tree", "-r", "-z", "HEAD").split(b"\0")
    result: dict[str, str] = {}
    for entry in entries:
        if not entry:
            continue
        metadata, raw_path = entry.split(b"\t", 1)
        _mode, kind, object_id = metadata.decode("ascii").split()
        if kind == "blob":
            result[object_id] = raw_path.decode("utf-8", errors="replace")
    return result


def historical_blobs() -> dict[str, str]:
    result: dict[str, str] = {}
    for line in run_git("rev-list", "--objects", "--all").splitlines():
        parts = line.split(b" ", 1)
        object_id = parts[0].decode("ascii")
        if len(parts) == 2:
            result.setdefault(object_id, parts[1].decode("utf-8", errors="replace"))
    return result


def load_baseline(path: Path | None) -> set[str]:
    if path is None or not path.exists():
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def scan_repository(mode: str, public_boundary: bool, baseline: set[str]) -> dict:
    current = current_blobs()
    objects = current if mode == "current" else historical_blobs()
    unique: dict[tuple[str, str], dict[str, str]] = {}
    skipped = 0
    for object_id in sorted(objects):
        try:
            if run_git("cat-file", "-t", object_id).strip() != b"blob":
                continue
            size = int(run_git("cat-file", "-s", object_id).strip())
            if size > MAX_BLOB_BYTES:
                skipped += 1
                continue
            data = run_git("cat-file", "blob", object_id)
        except (subprocess.CalledProcessError, ValueError):
            skipped += 1
            continue
        for finding in scan_bytes(data, public_boundary=public_boundary):
            key = (finding["category"], finding["alias"])
            if key not in unique:
                finding["reachable_from_head"] = str(object_id in current).lower()
                finding["baselined"] = str(finding["alias"] in baseline).lower()
                unique[key] = finding

    findings = sorted(unique.values(), key=lambda x: (x["severity"], x["alias"]))
    confirmed = [x for x in findings if x["severity"] == "confirmed"]
    unbaselined = [x for x in confirmed if x["alias"] not in baseline]
    return {
        "mode": mode,
        "public_boundary": public_boundary,
        "scanned_blob_count": len(objects),
        "skipped_blob_count": skipped,
        "confirmed_count": len(confirmed),
        "possible_count": len(findings) - len(confirmed),
        "baselined_confirmed_count": len(confirmed) - len(unbaselined),
        "unbaselined_confirmed_count": len(unbaselined),
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("current", "history"), default="current")
    parser.add_argument("--public-boundary", action="store_true")
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()
    report = scan_repository(
        args.mode, args.public_boundary, load_baseline(args.baseline)
    )
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    if args.report_only:
        return 0
    return 2 if report["unbaselined_confirmed_count"] else 0


if __name__ == "__main__":
    sys.exit(main())

