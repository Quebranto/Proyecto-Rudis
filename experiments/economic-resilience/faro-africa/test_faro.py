import copy
import unittest
from faro import evaluate

SCENE={'years':5,'discount_rate':0.1,'currency':'FICTIONAL','scenarios':[
{'name':'no_installation','capital_cost':0,'annual_fixed_cost':100,'annual_maintenance':0,'annual_extra_gross_margin':150,'annual_outage_loss':100,'annual_replacement':0,'annual_debt_service':0},
{'name':'distributed_power','capital_cost':1000,'annual_fixed_cost':100,'annual_maintenance':80,'annual_extra_gross_margin':600,'annual_outage_loss':10,'annual_replacement':20,'annual_debt_service':180}
]}
class Tests(unittest.TestCase):
    def test_positive_project(self):
        r=evaluate(SCENE)['scenarios'][0]
        self.assertEqual(r['name'],'distributed_power')
        self.assertTrue(r['passes_project_screen'])
    def test_reject_unviable(self):
        r=copy.deepcopy(SCENE)
        r['scenarios'][1]['annual_extra_gross_margin']=100
        self.assertEqual(evaluate(r)['scenarios'][-1]['screen'],'REJECT_OR_REDESIGN')
    def test_reject_debt_burden(self):
        r=copy.deepcopy(SCENE)
        r['scenarios'][1]['annual_debt_service']=1000
        self.assertEqual(evaluate(r)['scenarios'][0]['screen'],'REJECT_OR_REDESIGN')
    def test_reject_nan(self):
        r=copy.deepcopy(SCENE)
        r['scenarios'][1]['capital_cost']=float('nan')
        with self.assertRaises(ValueError): evaluate(r)
    def test_reject_negative(self):
        r=copy.deepcopy(SCENE)
        r['scenarios'][1]['annual_maintenance']=-1
        with self.assertRaises(ValueError): evaluate(r)
    def test_reject_invalid_years(self):
        r=copy.deepcopy(SCENE)
        r['years']=0
        with self.assertRaises(ValueError): evaluate(r)
    def test_no_double_count_debt_in_npv(self):
        r=copy.deepcopy(SCENE)
        r['scenarios'][1]['annual_debt_service']=1000
        original=evaluate(SCENE)['scenarios'][0]['project_npv']
        self.assertEqual(evaluate(r)['scenarios'][0]['project_npv'],original)
    def test_dup_names(self):
        r=copy.deepcopy(SCENE)
        r['scenarios'][1]['name']='no_installation'
        with self.assertRaises(ValueError): evaluate(r)
if __name__=='__main__': unittest.main()
