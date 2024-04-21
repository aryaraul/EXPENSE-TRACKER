from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for expenses
expenses = [
    
]

# Home route
@app.route('/')
def home():
    return render_template('index.html', expenses=expenses)

# Add expense route
@app.route('/add', methods=['POST'])
def add_expense():
    title = request.form['title']
    amount_inr = float(request.form['amount'])  # Assuming user enters amounts in INR
    expense = {'id': len(expenses) + 1, 'title': title, 'amount': amount_inr}
    expenses.append(expense)
    return redirect(url_for('home'))

# Delete expense route
@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    global expenses
    expenses = [expense for expense in expenses if expense['id'] != expense_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
