"""CONTRAPESO-04: independent, offline audit of an auditor's report."""
import json
import sys
from pathlib import Path

VALID_SEVERITY = {'low', 'medium', 'high', 'critical'}
VALID_CONFIDENCE = {'low', 'medium', 'high'}

def audit_report(report, case, source_audit):
    findings = []
    def flag(code, **details):
        findings.append({'code': code, **details})
    claims = {c['id']: c for c in case.get('claims', []) if isinstance(c, dict) and isinstance(c.get('id'), str)}
    sources = {s['id']: s for s in case.get('sources', []) if isinstance(s, dict) and isinstance(s.get('id'), str)}
    prior = source_audit.get('findings', [])
    by_claim = {}
    for item in prior:
        by_claim.setdefault(item.get('claim'), set()).add(item.get('code'))
    seen = set()
    for item in report.get('findings', []):
        fid = item.get('id')
        if not isinstance(fid, str) or not fid or fid in seen:
            flag('INVALID_FINDING_ID', finding=fid)
        seen.add(fid)
        cid = item.get('claim_id')
        if cid not in claims:
            flag('UNKNOWN_CLAIM', finding=fid, claim=cid)
            continue
        citations = item.get('source_ids', [])
        if not isinstance(citations, list) or not citations:
            flag('UNCITED_FINDING', finding=fid)
            citations = []
        for sid in citations:
            if sid not in sources:
                flag('UNKNOWN_CITATION', finding=fid, source=sid)
            elif not sources[sid].get('locator'):
                flag('UNTRACEABLE_CITATION', finding=fid, source=sid)
        if item.get('severity') not in VALID_SEVERITY:
            flag('INVALID_SEVERITY', finding=fid)
        if item.get('confidence') not in VALID_CONFIDENCE:
            flag('INVALID_CONFIDENCE', finding=fid)
        if not item.get('severity_rationale'):
            flag('UNJUSTIFIED_SEVERITY', finding=fid)
        if not item.get('counterargument'):
            flag('MISSING_COUNTERARGUMENT', finding=fid)
        if not item.get('falsification_test'):
            flag('MISSING_FALSIFICATION_TEST', finding=fid)
        if item.get('conclusion') == 'verified':
            blockers = {'CONTESTED_CLAIM', 'VERIFICATION_OVERCLAIM', 'UNKNOWN_ORIGIN', 'UNKNOWN_SOURCE', 'MISSING_LOCATOR', 'NO_EVIDENCE'}
            if claims[cid].get('status') != 'verified' or blockers.intersection(by_claim.get(cid, set())):
                flag('REPORT_OVERCLAIM', finding=fid, claim=cid)
        if item.get('recommended_action') in {'execute', 'sanction', 'censor', 'approve'}:
            flag('AUTHORITY_ESCALATION', finding=fid)
    if report.get('decision_authority') is not False:
        flag('AUTHORITY_CLAIM')
    if report.get('schema') != 'contrapeso.report.v04':
        flag('SCHEMA_MISMATCH')
    return {'schema': 'contrapeso.audit.v04', 'decision_authority': False,
            'findings': findings, 'passed_checks': len(findings) == 0,
            'limitations': ['Checks internal consistency, not factual truth.', 'Citations and declared origins are not independently authenticated.', 'Does not infer malicious intent.', 'No live news retrieval or deployment.']}

def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python contrapeso_v04.py expediente.json informe.json')
    paths = [Path(p) for p in sys.argv[1:]]
    for path in paths:
        if path.stat().st_size > 1_000_000:
            raise SystemExit('Input exceeds 1 MB')
    case, report = [json.loads(path.read_text(encoding='utf-8')) for path in paths]
    from contrapeso_v03 import audit
    print(json.dumps(audit_report(report, case, audit(case)), indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
