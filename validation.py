import calendar

CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Bills",
    "Shopping",
    "Health",
    "Education",
    "Travel",
    "Other"]

def get_amount(prompt):
    while True:
        text = input(prompt)
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        if "." in text and len(text.split(".")[1]) > 2:
            print("Please enter an amount with at most 2 decimal places.")
            continue

        return amount

def get_category(prompt):
    category = input(prompt)
    while category not in CATEGORIES:
        category = input("choose a valid category: ")
    return category

def get_year(prompt):
    while True:
        try:
            year = int(input(prompt))
            if 0 <= year <= 2100:
                return year
        except ValueError: 
            pass 
        print("Please enter a valid year.")

def get_month(prompt):
    while True:
        try:
            month = int(input(prompt))
            if 1 <= month <= 12:
                return month
        except ValueError: 
            pass 
        print("Please enter a valid month.")

def get_day(prompt, year, month):
    max_day = calendar.monthrange(year,month)[1]
    while True:
        try:
            day = int(input(prompt))
            if 1 <= day <= max_day:
                return day
        except ValueError: 
            pass 
        print("Please enter a valid day.")

def get_menu_choice():
    while True:
            try:
                choice = int(input("choose an option: "))
                if choice in [1, 2, 3, 4]:
                    return choice
            except ValueError:
                    pass
            print("Please enter a valid option.")

def get_text(prompt, max_length):
    while True:
        text = input(prompt)
        if len(text) == 0:
            print("This field cannot be empty.")
            continue
        if len(text) > max_length:
            print(f"Please enter at most {max_length} characters.")
            continue
        return text