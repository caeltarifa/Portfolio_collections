import unittest
from pyspark import SparkContext
from .CheapestOperator import CheapestOperator


class TestCheapestOperator(unittest.TestCase):

    def setUp(self):
        self.sc = SparkContext("local", "CheapestOperator")
        self.operators_url = {
            'OperatorA': './op_a.txt',
            'OperatorB': './op_b.txt',
            'OperatorC': './op_c.txt',
        }

    def tearDown(self):
        self.sc.stop()

    def test_cheapest_operator(self):
        number = "4673212345"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset(self.operators_url)
        self.assertEqual(obj.cheapest_operator(), ('OperatorA', 1.1))

    def test_invalid_number(self):
        number = "987654321"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset(self.operators_url)
        self.assertEqual(obj.cheapest_operator(), "No operator found for this number")

    def test_operator_B_only(self):
        number = "123456789"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset({'OperatorB': './op_b.txt'})
        self.assertEqual(obj.cheapest_operator(), ('OperatorB', 0.92))

    def test_logest_prefix(self):
        number = "4673210000"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset(self.operators_url)
        self.assertEqual(obj.cheapest_operator(), ('OperatorA', 1.1))

    def test_multiple_operators_same_price(self):
        number = "1234567890"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset(self.operators_url)
        self.assertEqual(obj.cheapest_operator(), ('OperatorA', 0.9))

    def test_single_operator_single_prefix(self):
        number = "123456789"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset({'OperatorA': './op_a.txt'})
        self.assertEqual(obj.cheapest_operator(), ('OperatorA', 0.9))

    def test_single_operator_multiple_prefixes(self):
        number = "4692114455"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset({'OperatorA': './op_a.txt'})
        self.assertEqual(obj.cheapest_operator(), ('OperatorA', 0.17))

    def test_same_price_different_operator(self):
        number = "2682114466"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset(self.operators_url)
        self.assertEqual(obj.cheapest_operator(), ('OperatorA', 5.1))

    def test_case_insensitive_dict(self):
        number = "4673212345"
        obj = CheapestOperator(number, self.sc)
        obj.setup_dataset({'operatora': './op_a.txt'})
        self.assertEqual(obj.cheapest_operator(), ('operatora', 1.1))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)