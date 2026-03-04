import sqlite3

# Create connection to SQLite database
def create_connection():
    conn = sqlite3.connect("expense.db")
    return conn


# Create expenses table
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        date TEXT,
        note TEXT
    )
    """)

    conn.commit()
    conn.close()


# Insert expense
def add_expense(amount, category, date, note):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
        (amount, category, date, note)
    )

    conn.commit()
    conn.close()


# Get all expenses
def get_expenses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    data = cursor.fetchall()

    conn.close()

    return data


# Delete expense
def delete_expense(expense_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))

    conn.commit()
    conn.close()