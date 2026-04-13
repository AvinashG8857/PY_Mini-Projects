import sqlite3

def init_db():
    conn= sqlite3.connect('receipts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
                   if INTEGER PRIMARY KEY AUTOINCREMENT,
                   customer_name TEXT NOT NULL,
                   item_description TEXT NOT NULL,
                   amount REAL NOT NULL,
                   date TEXT NOT NULL
                   )

    ''')

    conn.commit()
    conn.close()