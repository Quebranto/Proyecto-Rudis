#!/usr/bin/env python3
"""Offline, dependency-free repository security policy gate.

Output deliberately contains only finding codes and irreversible path aliases.
It never prints workflow contents or repository paths.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


PINNED_USE = re.compile(r"^[^@\s]+@[0-9a-fA-F]{40}$")
USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    locator: str


def locator_alias(value: str) -> str:
    return "LOC-" + hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def audit_workflow(text: str, locator: str) -> list[Finding]:
    findings: list[Finding] = []

    def add(code: str, severity: str = "HIGH") -> None:
        findings.append(Finding(code, severity, locator_alias(locator)))

    if re.search(r"(?m)^\s*(?:on\s*:\s*)?pull_request_target\s*:", text) or re.search(
        r"(?m)^\s*on\s*:\s*pull_request_target\s*$", text
    ):
        add("UNTRUSTED_PRIVILEGED_TRIGGER")
    if re.search(r"(?m)^\s*(?:on\s*:\s*)?workflow_run\s*:", text) or re.search(
        r"(?m)^\s*on\s*:\s*workflow_run\s*$", text
    ):
        add("PRIVILEGED_CHAIN_TRIGGER")
    if re.search(r"(?m)^\s*permissions\s*:\s*(write-all|read-all)?\s*$", text) is None:
        add("EXPLICIT_PERMISSIONS_MISSING")
    if re.search(r"(?m)^\s*permissions\s*:\s*write-all\s*$", text):
        add("WRITE_ALL_PERMISSIONS")
    for permission in ("contents", "actions", "checks", "packages", "pull-requests"):
        if re.search(rf"(?m)^\s*{re.escape(permission)}\s*:\s*write\s*$", text):
            add("WRITE_PERMISSION_PRESENT")
            break
    if re.search(r"(?m)^\s*id-token\s*:\s*write\s*$", text):
        add("OIDC_WRITE_REQUIRES_REVIEW", "MEDIUM")
    if re.search(r"(?m)^\s*persist-credentials\s*:\s*true\s*$", text):
        add("CHECKOUT_CREDENTIAL_PERSISTENCE")

    uses = USES.findall(text)
    for use in uses:
        if use.startswith("./"):
            continue
        if not PINNED_USE.fullmatch(use):
            add("ACTION_NOT_PINNED")
    if any(use.startswith("actions/checkout@") for use in uses) and not re.search(
        r"(?m)^\s*persist-credentials\s*:\s*false\s*$", text
    ):
        add("CHECKOUT_HARDENING_MISSING")

    if (re.search(r"(?m)^\s*pull_request\s*:", text) or re.search(r"(?m)^\s*on\s*:\s*pull_request\s*$", text)) and "secrets." in text:
        add("SECRET_IN_UNTRUSTED_PR")
    if re.search(r"(?s)run:\s*[|>-]?.*\$\{\{\s*github\.event\.pull_request\.(?:title|body|head\.ref)", text):
        add("UNTRUSTED_CONTEXT_IN_SHELL")
    return findings


def tracked_modes(root: Path) -> list[tuple[str, str]]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-s"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        return []
    rows: list[tuple[str, str]] = []
    for line in result.stdout.splitlines():
        fields = line.split(maxsplit=3)
        if len(fields) == 4:
            rows.append((fields[0], fields[3]))
    return rows


def audit_repository(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    workflow_root = root / ".github" / "workflows"
    for workflow in sorted(list(workflow_root.glob("*.yml")) + list(workflow_root.glob("*.yaml"))):
        findings.extend(audit_workflow(workflow.read_text(encoding="utf-8"), str(workflow.relative_to(root))))

    required = [root / ".github" / "CODEOWNERS", root / ".github" / "dependabot.yml"]
    for path in required:
        if not path.is_file():
            findings.append(Finding("REPOSITORY_CONTROL_MISSING", "MEDIUM", locator_alias(str(path.relative_to(root)))))
    if (root / ".gitmodules").exists():
        findings.append(Finding("SUBMODULE_REQUIRES_REVIEW", "MEDIUM", locator_alias(".gitmodules")))
    for mode, path in tracked_modes(root):
        if mode == "120000":
            findings.append(Finding("SYMLINK_REQUIRES_REVIEW", "MEDIUM", locator_alias(path)))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()
    findings = audit_repository(Path(args.root).resolve())
    by_severity = {severity: sum(f.severity == severity for f in findings) for severity in ("HIGH", "MEDIUM", "LOW")}
    print(json.dumps({
        "schema": "rudis.repository-policy-gate.v1",
        "finding_count": len(findings),
        "by_severity": by_severity,
        "findings": [f.__dict__ for f in findings],
    }, sort_keys=True))
    return 0 if args.report_only or by_severity["HIGH"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

