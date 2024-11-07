from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, request, redirect, flash, abort
from dbmodels import Expense, db

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']
        description = request.form['description']
        new_expense = Expense(amount, category, date, description)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('view_expenses'))
    return render_template('add_expense.html')

@app.route('/expenses')
def view_expenses():
    expenses = Expense.query.all()
    return render_template('view_expenses.html', expenses=expenses)

@app.route('/edit/<int:id>', methods = ['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        expense.amount = request.form['amount']
        expense.category = request.form['category']
        expense.date = request.form['date']
        expense.description = request.form['description']
        db.session.commit()
        return redirect(url_for('view_expenses'))
    return render_template('edit_expense.html', expense=expense)

@app.route('/delete/<int:id>', methods = ['GET', 'POST'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('view_expenses'))