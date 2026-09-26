import datetime
import database
import validation
import reports

def add_income():
    amount = validation.get_amount("amount: £")
    category = validation.get_text("category: ", 14)
    description = validation.get_text("description: ", 19)

    database.insert_transaction(
        datetime.datetime.now().isoformat(),
        "Income",
        amount,
        category,
        description
    )
    print("\nIncome added")

def add_expense():
    balance = reports.get_balance()
    amount = validation.get_amount("amount: £")
    while amount > balance:
        print(f"Insufficient balance (£{balance:.2f} available).")
        amount = validation.get_amount("amount: £")
    category = validation.get_category("category: ")
    description = validation.get_text("description: ", 19)

    database.insert_transaction(
        datetime.datetime.now().isoformat(),
        "Expense",
        amount,
        category,
        description
    )
    print("\nExpense added")

def get_date_range(category_option):
    startD, endD, startM, endM, startY, endY = 1, 31, 1, 12, 2000, 2100

    if category_option > 1:
        startY = validation.get_year("Enter start year: ")
        endY = validation.get_year("Enter end year: ")

    if category_option > 2:
        startM = validation.get_month("Enter start month: ")
        endM = validation.get_month("Enter end month: ")

    if category_option > 3:
        startD = validation.get_day("Enter start date ", startY, startM)
        endD = validation.get_day("Enter end date: ", endY, endM)

    start_dt = datetime.datetime(startY, startM, startD)
    end_dt = datetime.datetime(endY, endM, endD, 23, 59, 59, 9999)
    return start_dt.isoformat(), end_dt.isoformat()