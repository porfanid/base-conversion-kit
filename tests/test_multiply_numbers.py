import unittest
from base_conversion_kit import multiply_numbers


class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_numbers_positive(self):
        result = multiply_numbers("2", "3", 10)
        self.assertEqual(result, "6")

    def test_multiply_numbers_large_result(self):
        result = multiply_numbers("FF", "2", 16)
        self.assertEqual(result, "1FE")
