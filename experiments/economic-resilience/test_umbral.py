import tempfile
import unittest
from pathlib import Path
from decimal import Decimal
from umbral import calculate, compare

BASE = dict(provider="A",budget="200",upfront_fee="5",deducted_fee="0",fx_rate=".9",recipient_fee="0",reference_rate=".92",hours="24",verified_at="DEMO")

class RemittanceTests(unittest.TestCase):
    def test_net(self):
        q = calculate(BASE)
        self.assertEqual(q["received"],Decimal("175.5"))
        self.assertEqual(q["cost_pct"],Decimal("100") * Decimal("8.5") / Decimal("184"))
    def test_deducted(self):
        self.assertEqual(calculate({**BASE, "deducted_fee":"5"})["received"], Decimal("171"))
    def test_too_large_fee(self):
        with self.assertRaises(ValueError): calculate({**BASE,"upfront_fee":"201"})
    def test_negative(self):
        with self.assertRaises(ValueError): calculate({**BASE,"recipient_fee":"-1"})
    def test_nan(self):
        with self.assertRaises(ValueError): calculate({**BASE,"fx_rate":"NaN"})
    def test_rank_and_filter(self):
        csv_data = "provider,budget,upfront_fee,deducted_fee,fx_rate,recipient_fee,reference_rate,hours,verified_at\nA,200,5,0,.9,0,.92,24,DEMO\nB,200,0,0,.92,0,.92,48,DEMO\n"
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory)/"quotes.csv"
            file.write_text(csv_data)
            self.assertEqual(compare(file)[0]["provider"],"B")
            self.assertEqual(compare(file,Decimal("24"))[0]["provider"],"A")
    def test_reject_mixed_budgets(self):
        csv_data = "provider,budget,upfront_fee,deducted_fee,fx_rate,recipient_fee,reference_rate,hours,verified_at\nA,200,5,0,.9,0,.92,24,DEMO\nB,300,0,0,.92,0,.92,48,DEMO\n"
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory)/"quotes.csv"
            file.write_text(csv_data)
            with self.assertRaisesRegex(ValueError,"presupuestos"): compare(file)

if __name__=="__main__": unittest.main()
