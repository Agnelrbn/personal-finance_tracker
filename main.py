import database
import operations
import reports
import validation

def menu():
    while True:
        print("""
        =========================
        Personal Finance Tracker
        =========================
        """)
        print(f"        Balance: £{reports.get_balance():.2f}")
        print("""
        1. Add income
        2. Add expense
        3. View transactions
        4. View spending by category
        5. Exit
        """)
        option = input("Choose an option: ")

        if option == "1":
            operations.add_income()

        elif option == "2":
            operations.add_expense()

        elif option == "3":
            print("""
        1. View whole transactions
        2. view by year
        3. view by month
        4. View by date
        """)
            choice = validation.get_menu_choice()
            start, end = operations.get_date_range(choice)
            reports.view_transactions(start, end)

        elif option == "4":
            print("""
        1. View whole expenses
        2. view by year
        3. view by month
        4. View by date
        """)
            choice = validation.get_menu_choice()
            start, end = operations.get_date_range(choice)
            reports.view_spending_by_category(start, end)

        elif option == "5":
            break

        else:
            print("\nChoose a valid option")

if __name__ == "__main__":
    database.create_table()
    menu()