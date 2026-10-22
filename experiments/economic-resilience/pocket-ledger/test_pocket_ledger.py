import tempfile
import unittest
from pathlib import Path
from pocket_ledger import summarize

HEADER="date,category,income,expense,note\n"
def run(rows):
    with tempfile.TemporaryDirectory() as tmp:
        file=Path(tmp)/"test.csv"
        file.write_text(HEADER+rows,encoding="utf-8")
        return summarize(file)

class Tests(unittest.TestCase):
    def test_net(self):
        self.assertEqual(run("2026-01-01,trade,12.50,0,sale\n2026-01-02,trade,0,2.25,fee\n")["trade"]["net"],"10.25")
    def test_empty(self):
        self.assertEqual(run(""),{})
    def test_negative(self):
        with self.assertRaises(ValueError): run("2026-01-01,trade,-2,0,bad\n")
    def test_nan(self):
        with self.assertRaises(ValueError): run("2026-01-01,trade,NaN,0,bad\n")
    def test_dual(self):
        with self.assertRaises(ValueError): run("2026-01-01,trade,1,1,bad\n")
    def test_precision(self):
        with self.assertRaises(ValueError): run("2026-01-01,trade,0.001,0,bad\n")

if __name__=="__main__":
    unittest.main()
