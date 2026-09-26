import unittest
from unittest.mock import patch
import os

import database
import operations
import reports


class TestOperations(unittest.TestCase):
    def setUp(self):
        database.DB_NAME = "test_transactions.db"
        if os.path.exists(database.DB_NAME):
            os.remove(database.DB_NAME)
        database.create_table()

    def tearDown(self):
        if os.path.exists(database.DB_NAME):
            os.remove(database.DB_NAME)

    def test_income_increases_balance(self):
        with patch('builtins.input', side_effect=["100", "Salary", "September pay"]):
            operations.add_income()
        self.assertEqual(reports.get_balance(), 100.0)

    def test_income_then_expense(self):
        with patch('builtins.input', side_effect=["100", "Salary", "September pay"]):
            operations.add_income()
        with patch('builtins.input', side_effect=["30", "Food", "Lunch"]):
            operations.add_expense()
        self.assertEqual(reports.get_balance(), 70.0)

    def test_income_then_two_expenses(self):
        with patch('builtins.input', side_effect=["100", "Salary", "September pay"]):
            operations.add_income()
        with patch('builtins.input', side_effect=["30", "Food", "Lunch"]):
            operations.add_expense()
        with patch('builtins.input', side_effect=["20", "Food", "Dinner"]):
            operations.add_expense()
        self.assertEqual(reports.get_balance(), 50.0)

    def test_expense_exceeding_balance_is_rejected_then_retried(self):
        with patch('builtins.input', side_effect=["50", "Salary", "pay"]):
            operations.add_income()
        with patch('builtins.input', side_effect=["100", "40", "Food", "Groceries"]):
            operations.add_expense()
        self.assertEqual(reports.get_balance(), 10.0)

    def test_invalid_category_in_expense_is_rejected_then_retried(self):
        with patch('builtins.input', side_effect=["100", "Salary", "pay"]):
            operations.add_income()
        with patch('builtins.input', side_effect=["10", "NotACategory", "Food", "Snack"]):
            operations.add_expense()
        self.assertEqual(reports.get_balance(), 90.0)


if __name__ == "__main__":
    unittest.main()