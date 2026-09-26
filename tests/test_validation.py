import unittest
from unittest.mock import patch

import validation


class TestGetAmount(unittest.TestCase):
    def test_negative_amount_is_rejected(self):
        with patch('builtins.input', side_effect=["-10", "20"]):
            amount = validation.get_amount("amount: ")
        self.assertEqual(amount, 20.0)

    def test_zero_is_rejected(self):
        with patch('builtins.input', side_effect=["0", "5"]):
            amount = validation.get_amount("amount: ")
        self.assertEqual(amount, 5.0)

    def test_non_numeric_input_is_rejected(self):
        with patch('builtins.input', side_effect=["abc", "15"]):
            amount = validation.get_amount("amount: ")
        self.assertEqual(amount, 15.0)

    def test_too_many_decimal_places_is_rejected(self):
        with patch('builtins.input', side_effect=["10.999", "10.99"]):
            amount = validation.get_amount("amount: ")
        self.assertEqual(amount, 10.99)

    def test_two_decimal_places_is_accepted(self):
        with patch('builtins.input', side_effect=["19.99"]):
            amount = validation.get_amount("amount: ")
        self.assertEqual(amount, 19.99)

    def test_whole_number_is_accepted(self):
        with patch('builtins.input', side_effect=["50"]):
            amount = validation.get_amount("amount: ")
        self.assertEqual(amount, 50.0)


class TestGetCategory(unittest.TestCase):
    def test_invalid_category_is_rejected(self):
        with patch('builtins.input', side_effect=["NotACategory", "Food"]):
            category = validation.get_category("category: ")
        self.assertEqual(category, "Food")

    def test_valid_category_is_accepted_immediately(self):
        with patch('builtins.input', side_effect=["Bills"]):
            category = validation.get_category("category: ")
        self.assertEqual(category, "Bills")


class TestGetText(unittest.TestCase):
    def test_empty_description_is_rejected(self):
        with patch('builtins.input', side_effect=["", "Groceries"]):
            text = validation.get_text("description: ", 20)
        self.assertEqual(text, "Groceries")

    def test_description_over_max_length_is_rejected(self):
        too_long = "x" * 21
        with patch('builtins.input', side_effect=[too_long, "short"]):
            text = validation.get_text("description: ", 20)
        self.assertEqual(text, "short")

    def test_description_at_exact_max_length_is_accepted(self):
        exactly_20 = "x" * 20
        with patch('builtins.input', side_effect=[exactly_20]):
            text = validation.get_text("description: ", 20)
        self.assertEqual(text, exactly_20)


if __name__ == "__main__":
    unittest.main()