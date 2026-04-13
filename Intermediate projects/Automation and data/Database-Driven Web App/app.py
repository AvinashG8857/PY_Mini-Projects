from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    """Establishes a connection to the database."""
    conn = sqlite3.connect('expenese tracker\expenses.db')
    # Row_factory allows us to access columns by name (like row['amount']) 
    # instead of just index (row[1])
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    """The Home Page: Displays all expenses."""
    conn = get_db_connection()
    # Fetch all records to show in a table
    expenses = conn.execute('SELECT * FROM expenses').fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=('POST',))
def add_expense():
    """Handles the form submission to add a new expense."""
    # Getting data from the HTML form 'name' attributes
    amount = request.form['amount']
    category = request.form['category']
    description = request.form['description']
    date = request.form['date']

    conn = get_db_connection()
    conn.execute('INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)',
                 (amount, category, description, date))
    conn.commit()
    conn.close()
    
    # After saving, go back to the home page
    return redirect('/')

if __name__ == '__main__':
    # Start the local development server
    app.run(debug=True)