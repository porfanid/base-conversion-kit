import unittest
from base_conversion_kit import subtract_numbers


class TestSubtractNumbers(unittest.TestCase):

    def test_subtract_numbers_positive(self):
        result = subtract_numbers("30", "10", 10)
        self.assertEqual(result, "20")

    def test_subtract_numbers_negative(self):
        with self.assertRaises(ValueError):
            subtract_numbers("10", "20", 10)
