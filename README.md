# Personal Finance Tracker

A Python-based personal finance tracker for managing income and expenses from the command line.

## Features

- Add income
- Add expenses
- Categorise transactions
- Calculate balance
- View transactions and spending by category, filtered by date range
- Persistent storage using SQLite
- Input validation (amounts, categories, text length)
- Automated tests (unittest)

## Technologies

- Python
- SQLite
- Git
- unittest

## Project structure

personal-finance-tracker/
├── main.py # Entry point, menu loop
├── database.py # SQLite connection and queries
├── operations.py # Add income / add expense logic
├── reports.py # Balance, transaction view, spending by category
├── validation.py # Input validation helpers
├── tests/ # Automated tests
├── .gitignore
└── README.md


## How to run

1. Clone the repository:
```bash
   git clone https://github.com/YOUR-USERNAME/personal-finance-tracker.git
   cd personal-finance-tracker
```

2. Make sure you have Python 3 installed (check with `python3 --version`).

3. Run the program:
```bash
   python3 main.py
```

   On first run, the program automatically creates a local `transactions.db` file to store your data.

## Running the tests

```bash
python3 -m unittest discover tests
```

## Usage

When you run the program, you'll see a menu:

1. Add income
2. Add expense
3. View transactions
4. View spending by category
5. Exit

Follow the prompts to enter amounts, categories, and descriptions. Balance is calculated automatically from all stored transactions.
