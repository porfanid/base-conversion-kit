import unittest
from base_conversion_kit import convert_base


class TestConvertBase(unittest.TestCase):

    def test_convert_base_positive(self):
        result = convert_base("1010", 2, 16)
        self.assertEqual(result, "A")

    def test_convert_base_invalid_base(self):
        with self.assertRaises(ValueError):
            convert_base("1010", 1, 16)

