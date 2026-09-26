import unittest
import os
import datetime

import database
import reports


class TestReports(unittest.TestCase):
    def setUp(self):
        database.DB_NAME = "test_transactions.db"
        if os.path.exists(database.DB_NAME):
            os.remove(database.DB_NAME)
        database.create_table()

    def tearDown(self):
        if os.path.exists(database.DB_NAME):
            os.remove(database.DB_NAME)

    def test_balance_reflects_all_transactions(self):
        database.insert_transaction(datetime.datetime(2026, 1, 1).isoformat(), "Income", 200.0, "Salary", "Jan pay")
        database.insert_transaction(datetime.datetime(2026, 9, 1).isoformat(), "Expense", 50.0, "Food", "Groceries")
        self.assertEqual(reports.get_balance(), 150.0)

    def test_monthly_category_total_excludes_other_months(self):
        database.insert_transaction(datetime.datetime(2026, 9, 10).isoformat(), "Expense", 30.0, "Food", "Groceries")
        database.insert_transaction(datetime.datetime(2026, 10, 5).isoformat(), "Expense", 50.0, "Food", "Takeaway")

        start = datetime.datetime(2026, 9, 1).isoformat()
        end = datetime.datetime(2026, 9, 30, 23, 59, 59, 999999).isoformat()

        total = database.get_category_total("Food", start, end)
        self.assertEqual(total, 30.0)

    def test_monthly_category_total_is_zero_with_no_matches(self):
        database.insert_transaction(datetime.datetime(2026, 9, 10).isoformat(), "Expense", 30.0, "Bills", "Gas")

        start = datetime.datetime(2026, 9, 1).isoformat()
        end = datetime.datetime(2026, 9, 30, 23, 59, 59, 999999).isoformat()

        total = database.get_category_total("Food", start, end)
        self.assertEqual(total, 0)

    def test_transactions_before_range_are_brought_forward_correctly(self):
        database.insert_transaction(datetime.datetime(2026, 1, 1).isoformat(), "Income", 100.0, "Salary", "Jan pay")
        database.insert_transaction(datetime.datetime(2026, 9, 10).isoformat(), "Expense", 20.0, "Food", "Lunch")

        rows_before = database.get_rows_before(datetime.datetime(2026, 9, 1).isoformat())
        brought_forward = sum(a if t == "Income" else -a for t, a in rows_before)
        self.assertEqual(brought_forward, 100.0)


if __name__ == "__main__":
    unittest.main()