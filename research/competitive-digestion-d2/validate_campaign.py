"""Offline fail-closed validator for the D2 competitive-digestion manifest."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


COMMIT = re.compile(r"^[0-9a-f]{40}$")
TRACKS = {"deep-digestion", "parallel-dossier"}
SOURCE_STATES = {
    "IDENTITY_RESOLVED",
    "ACRONYM_AMBIGUOUS",
    "MULTIREPO_SNAPSHOT_INCOMPLETE",
    "IDENTITY_CANDIDATE",
}
FORBIDDEN = {"AuthorityResolver", "LawEngine", "SovereignKernel", "ContinuityLedger"}


class ManifestError(ValueError):
    pass


def validate(data: dict) -> None:
    if data.get("schema_version") != "rudis-competitive-digestion-manifest/0.1":
        raise ManifestError("unknown schema version")
    if data.get("maximum_phase") != "D2":
        raise ManifestError("campaign phase must remain D2")
    if data.get("runtime_network_allowed") is not False:
        raise ManifestError("runtime network must be disabled")
    if data.get("production_accreditation") is not False:
        raise ManifestError("manifest cannot accredit production")

    entries = data.get("entries")
    if not isinstance(entries, list) or len(entries) != 5:
        raise ManifestError("exactly five source entries are required")

    ids: set[str] = set()
    repositories: set[str] = set()
    for entry in entries:
        entry_id = entry.get("id")
        repository = entry.get("repository")
        if not isinstance(entry_id, str) or not entry_id:
            raise ManifestError("entry id is required")
        if entry_id in ids:
            raise ManifestError(f"duplicate entry id: {entry_id}")
        ids.add(entry_id)
        if not isinstance(repository, str) or not repository.startswith("https://github.com/"):
            raise ManifestError(f"invalid repository for {entry_id}")
        if repository in repositories:
            raise ManifestError(f"duplicate repository: {repository}")
        repositories.add(repository)
        if not COMMIT.fullmatch(str(entry.get("commit", ""))):
            raise ManifestError(f"unsealed commit for {entry_id}")
        if entry.get("track") not in TRACKS:
            raise ManifestError(f"unknown track for {entry_id}")
        if entry.get("source_status") not in SOURCE_STATES:
            raise ManifestError(f"unknown source status for {entry_id}")
        if not entry.get("license"):
            raise ManifestError(f"missing license observation for {entry_id}")

    boundary = data.get("integration_boundary", {})
    if boundary.get("allowed_ingress") != ["ExternalEvidence"]:
        raise ManifestError("external material may enter only as ExternalEvidence")
    if set(boundary.get("forbidden_direct_consumers", [])) != FORBIDDEN:
        raise ManifestError("sovereign direct-consumer boundary changed")
    if boundary.get("external_conformance_grants_authority") is not False:
        raise ManifestError("conformance cannot grant authority")
    if boundary.get("technical_consent_is_juridical_mandate") is not False:
        raise ManifestError("technical consent cannot become juridical mandate")


def main(path: Path) -> int:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        validate(data)
    except (OSError, json.JSONDecodeError, ManifestError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print("VALID: sealed D2 campaign manifest")
    return 0


if __name__ == "__main__":
    default = Path(__file__).with_name("campaign-manifest-v0.1.json")
    raise SystemExit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else default))

