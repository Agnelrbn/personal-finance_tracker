import datetime
import database
import validation

def get_balance():
    rows = database.get_all_rows()
    balance = 0.0
    for type_, amount in rows:
        balance += amount if type_ == "Income" else -amount
    return balance

def view_transactions(start, end):
    print("\n" + f"{'Date':<12} {'Type':<10} {'Amount':>10}   {'Category':<15} {'Description':<20}")
    print("-" * 80)

    balance_brought_forward = 0.0
    for type_, amount in database.get_rows_before(start):
        balance_brought_forward += amount if type_ == "Income" else -amount

    print(f"{"BALANCE BROUGHT FORWARD":<25}£{balance_brought_forward:.2f}" + "\n")

    running_balance = balance_brought_forward
    for date_str, type_, amount, category, description in database.get_rows_in_range(start, end):
        date_obj = datetime.datetime.fromisoformat(date_str)
        print(
            f"{date_obj.strftime('%d/%m/%Y'):<12} "
            f"{type_:<10} "
            f"{amount:>10.2f}   "
            f"{category:<15} "
            f"{description:<20}"
        )
        running_balance += amount if type_ == "Income" else -amount
                
    print("\n" + f"{"BALANCE CARRIED FORWARD":<25}£{running_balance:.2f}")

def view_spending_by_category(start, end):
    print("\nSpending by category\n")
    for category in validation.CATEGORIES:
        total = database.get_category_total(category, start, end)
        print(f"{category:<15} £{total:.2f}")