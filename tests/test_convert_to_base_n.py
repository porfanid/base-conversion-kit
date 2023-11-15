import unittest
from base_conversion_kit import convert_to_base_n


class TestConvertToBaseN(unittest.TestCase):

    def test_convert_to_base_n_positive(self):
        result = convert_to_base_n(10, 2)
        self.assertEqual(result, "1010")

    def test_convert_to_base_n_zero(self):
        result = convert_to_base_n(0, 16)
        self.assertEqual(result, "0")

    def test_convert_to_base_n_large_number(self):
        result = convert_to_base_n(255, 16)
        self.assertEqual(result, "FF")
