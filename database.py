import sqlite3

DB_NAME = "transactions.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        type TEXT,
        amount REAL,
        category TEXT,
        description TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_transaction(date, type_, amount, category, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (date, type, amount, category, description) VALUES (?, ?, ?, ?, ?)",
        (date, type_, amount, category, description)
    )
    conn.commit()
    conn.close()

def get_all_rows():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    rows = cursor.execute("SELECT type, amount FROM transactions").fetchall()
    conn.close()
    return rows

def get_rows_before(date_str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    rows = cursor.execute(
        "SELECT type, amount FROM transactions WHERE date < ?",
        (date_str,)
    ).fetchall()
    conn.close()
    return rows

def get_rows_in_range(start, end):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    rows = cursor.execute(
        "SELECT date, type, amount, category, description FROM transactions WHERE date >= ? AND date <= ?",
        (start, end)
    ).fetchall()
    conn.close()
    return rows

def get_category_total(category, start, end):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    rows = cursor.execute(
        "SELECT amount FROM transactions WHERE type = 'Expense' AND category = ? AND date >= ? AND date <= ?",
        (category, start, end)
    ).fetchall()
    conn.close()
    return sum(r[0] for r in rows)