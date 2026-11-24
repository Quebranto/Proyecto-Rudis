"""CONTRAPESO-03: offline, consultative claim/source provenance checks."""
import json
import sys
from collections import defaultdict
from pathlib import Path

VALID_STANCES = {'supports', 'refutes'}

def audit(case):
    findings = []
    sources = {}
    for s in case.get('sources', []):
        sid = s.get('id')
        if not sid or sid in sources:
            findings.append({'code': 'SOURCE_ID_INVALID', 'source': sid})
            continue
        sources[sid] = s
    for claim in case.get('claims', []):
        cid = claim.get('id', '(missing)')
        evidence = claim.get('evidence', [])
        if not evidence:
            findings.append({'code': 'NO_EVIDENCE', 'claim': cid})
        groups = defaultdict(set)
        stances = defaultdict(set)
        for item in evidence:
            sid, stance = item.get('source_id'), item.get('stance')
            if sid not in sources:
                findings.append({'code': 'UNKNOWN_SOURCE', 'claim': cid, 'source': sid})
                continue
            if stance not in VALID_STANCES:
                findings.append({'code': 'INVALID_STANCE', 'claim': cid, 'source': sid})
                continue
            s = sources[sid]
            origin = s.get('origin_id')
            if not origin:
                findings.append({'code': 'UNKNOWN_ORIGIN', 'claim': cid, 'source': sid})
                origin = f'unknown:{sid}'
            groups[stance].add(origin)
            stances[origin].add(stance)
            if not s.get('locator'):
                findings.append({'code': 'MISSING_LOCATOR', 'claim': cid, 'source': sid})
        if len(groups['supports']) == 1 and len([i for i in evidence if i.get('stance') == 'supports']) > 1:
            findings.append({'code': 'SINGLE_ORIGIN_ECHO', 'claim': cid})
        if groups['supports'] and groups['refutes']:
            findings.append({'code': 'CONTESTED_CLAIM', 'claim': cid})
        for origin, positions in stances.items():
            if len(positions) > 1:
                findings.append({'code': 'INCONSISTENT_ORIGIN', 'claim': cid, 'origin': origin})
        if claim.get('status') == 'verified' and (not groups['supports'] or groups['refutes'] or any(f.get('claim') == cid and f['code'] in ('UNKNOWN_ORIGIN', 'UNKNOWN_SOURCE', 'MISSING_LOCATOR') for f in findings)):
            findings.append({'code': 'VERIFICATION_OVERCLAIM', 'claim': cid})
    return {'schema': 'contrapeso.v03', 'decision_authority': False, 'findings': findings,
            'limitations': ['Declared source origins are not authenticated.', 'No semantic truth verification.', 'No live network retrieval.', 'Findings are review prompts, not verdicts.']}

def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python contrapeso_v03.py expediente.json')
    path = Path(sys.argv[1])
    if path.stat().st_size > 1_000_000:
        raise SystemExit('Case too large')
    print(json.dumps(audit(json.loads(path.read_text(encoding='utf-8'))), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
