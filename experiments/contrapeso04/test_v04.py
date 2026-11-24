import unittest
from contrapeso_v03 import audit
from contrapeso_v04 import audit_report
import copy

CASE = {'sources': [{'id':'a','origin_id':'press','locator':'https://example.org/a'}, {'id':'b','origin_id':'press','locator':'https://example.org/b'}, {'id':'c','origin_id':'other','locator':'https://example.org/c'}], 'claims':[{'id':'claim1','status':'verified','evidence':[{'source_id':'a','stance':'supports'},{'source_id':'b','stance':'supports'},{'source_id':'c','stance':'refutes'}]}]}
BASE = {'schema':'contrapeso.report.v04','decision_authority':False,'findings':[{'id':'f1','claim_id':'claim1','source_ids':['a','c'],'severity':'high','confidence':'medium','severity_rationale':'Potential impact, not proof','counterargument':'Contrary evidence may be mistaken','falsification_test':'Check independent records','conclusion':'contested','recommended_action':'review'}]}

def codes(report, case=CASE):
    return {f['code'] for f in audit_report(report, case, audit(case))['findings']}

class Tests(unittest.TestCase):
    def test_clean_report(self): self.assertEqual(codes(BASE), set())
    def test_overclaim(self):
        r=copy.deepcopy(BASE); r['findings'][0]['conclusion']='verified'
        self.assertIn('REPORT_OVERCLAIM',codes(r))
    def test_authority(self):
        r=copy.deepcopy(BASE); r['decision_authority']=True
        self.assertIn('AUTHORITY_CLAIM',codes(r))
    def test_automated_sanction(self):
        r=copy.deepcopy(BASE); r['findings'][0]['recommended_action']='sanction'
        self.assertIn('AUTHORITY_ESCALATION',codes(r))
    def test_unknown_citation(self):
        r=copy.deepcopy(BASE); r['findings'][0]['source_ids']=['fake']
        self.assertIn('UNKNOWN_CITATION',codes(r))
    def test_missing_falsification(self):
        r=copy.deepcopy(BASE); r['findings'][0]['falsification_test']=''
        self.assertIn('MISSING_FALSIFICATION_TEST',codes(r))
    def test_unjustified_severity(self):
        r=copy.deepcopy(BASE); r['findings'][0]['severity_rationale']=''
        self.assertIn('UNJUSTIFIED_SEVERITY',codes(r))
    def test_uncited(self):
        r=copy.deepcopy(BASE); r['findings'][0]['source_ids']=[]
        self.assertIn('UNCITED_FINDING',codes(r))
    def test_duplicate_finding(self):
        r=copy.deepcopy(BASE); r['findings'].append(copy.deepcopy(r['findings'][0]))
        self.assertIn('INVALID_FINDING_ID',codes(r))
    def test_untraceable(self):
        case=copy.deepcopy(CASE);case['sources'][0]['locator']=''
        self.assertIn('UNTRACEABLE_CITATION',codes(BASE,case))

if __name__=='__main__': unittest.main()
