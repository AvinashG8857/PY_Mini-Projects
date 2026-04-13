import sqlite3
from datetime import datetime
from database import init_db
from pdf_generator import generate_pdf

def add_receipt():
    # Collect data from user
    name = input("Customer Name: ")
    item = input("Item/Service: ")
    
    # Basic error handling: if user enters text for price, the app won't crash
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    # Generate a timestamp (Year-Month-Day Hour:Minute)
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Database Insertion
    conn = sqlite3.connect('receipts.db')
    cursor = conn.cursor()
    
    # Using '?' placeholders prevents "SQL Injection" (a major security risk)
    cursor.execute('''
        INSERT INTO receipts (customer_name, item_description, amount, date) 
        VALUES (?, ?, ?, ?)
    ''', (name, item, amount, date))
    
    # Get the ID that was just created by AUTOINCREMENT
    receipt_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    # Trigger the PDF generation using the data we just saved
    file = generate_pdf(receipt_id, name, item, amount, date)
    print(f"\n✅ Success! Receipt #{receipt_id} generated as {file}")

def view_receipts():
    """Fetches and displays all records from the database."""
    conn = sqlite3.connect('receipts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM receipts')
    rows = cursor.fetchall() # Returns a list of tuples
    
    print("\n--- RECEIPT LOG ---")
    for row in rows:
        # row[0] is ID, row[1] is Name, etc. based on our Schema
        print(f"[{row[0]}] {row[4]} | {row[1]} | ${row[3]}")
    conn.close()

def main():
    # Ensure the table exists before we try to use it
    init_db()
    
    while True:
        print("\n--- Receipt Book Menu ---")
        print("1. Create New Receipt")
        print("2. View Receipt History")
        print("3. Exit")
        
        choice = input("Select (1-3): ")
        
        if choice == '1':
            add_receipt()
        elif choice == '2':
            view_receipts()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    # This ensures the app only runs if the script is executed directly
    main()