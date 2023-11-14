import unittest
from base_conversion_kit import add_numbers


class TestAddNumbers(unittest.TestCase):

    def test_add_numbers_positive(self):
        result = add_numbers("10", "20", 10)
        self.assertEqual(result, "30")

    def test_add_numbers_negative(self):
        result = add_numbers("FF", "01", 16)
        self.assertEqual(result, "100")
