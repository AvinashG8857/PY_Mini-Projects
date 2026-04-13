import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def add_expenses(amount,category,description):
    date=datetime.now().strftime("%Y-%m-%d")
    conn= sqlite3.connect("expenses.db")
    cursor=conn.cursor()

    cursor.execute('''
            INSERT INTO expenses (amount, category,description,date)
            VALUES(?,?,?,?)       
    ''',(amount,category,description,date))
    conn.commit()
    conn.close()

def generate_report():
    conn= sqlite3.connect("expenses.db")
    df=pd.read_sql_query("SELECT * FROM expenses",conn)
    conn.close()

    if df.empty:
        print("No expenses recorded yet")
        return
    
    summary= df.groupby("category")["amount"].sum()
    print("\n---- SPENDING BREAKDOWN -----")
    print(summary)

    summary.plot(kind="pie",autopct="%1.1f%%",title="Where is your MOney spent")
    plt.ylabel("")
    plt.show()
