import unittest
from benchmark_notebook import summarize
class Tests(unittest.TestCase):
    def test_summary(self):
        result=summarize([5,1,3,2,4])
        self.assertEqual(result["mean"],3)
        self.assertEqual(result["median"],3)
        self.assertEqual(result["p95"],5)
    def test_single(self):
        self.assertEqual(summarize([10])["p99"],10)
    def test_reject_empty(self):
        with self.assertRaises(ValueError): summarize([])
    def test_reject_nan(self):
        with self.assertRaises(ValueError): summarize([float("nan")])
    def test_reject_bool(self):
        with self.assertRaises(ValueError): summarize([True])
if __name__=="__main__": unittest.main()
