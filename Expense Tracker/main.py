# Expense Tracker OOPS Code
import sqlite3
from datetime import datetime

class Expenses:
    def __init__(self, category, amount, user, date):
        self.category = category
        self.amount = amount
        self.user = user
        self.date = date

    def __str__(self):
        return f"{self.category} {self.amount} {self.user} {self.date}"
    
class Budget:
    def __init__(self, category=None, user=None, amount=0):
        self.category = category
        self.user = user
        self.amount = amount
        self.spent = 0

    def update_budget(self, spent_amount):
        self.spent += spent_amount
    
    def remaining_budget(self):
        return self.amount - self.spent

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budgets = []
        self.db = sqlite3.connect('expense_tracker.db')
        self.create_tables()
    
    def create_tables(self):
        with self.db:
            self.db.execute('''CREATE TABLE IF NOT EXISTS expenses
                            (category TEXT, amount REAL, user TEXT, date TEXT) ''')
            self.db.execute('''CREATE TABLE IF NOT EXISTS budgets
                            (category TEXT, user TEXT, amount REAL, spent REAL)''')
        
    def add_expense(self, category, amount, user, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        expense = Expenses(category, amount, user, date)
        self.expenses.append(expense)
        
        with self.db:
            self.db.execute('INSERT INTO expenses (category, amount, user, date) VALUES (?, ?, ?, ?)',
                            (category, amount, user, date))
        
        print(f"Expense added: {expense}")
        return expense

    def set_budget(self, category, user, amount):
        budget = Budget(category, user, amount)
        self.budgets.append(budget)
        with self.db:
            self.db.execute('INSERT INTO budgets (category, user, amount, spent) VALUES (?, ?, ?, ?)',
                            (category, user, amount, 0))
        
        print(f"Budget set for {user} on {category}: {amount}")

        return budget
    
    def view_summary(self):
        print("\nExpense Summary")
        for budget in self.budgets:
            print(f"Category: {budget.category}, User: {budget.user}, Budget: {budget.amount}, Spent: {budget.spent}, Remaining: {budget.remaining_budget()}")

    def track_by_user(self, user):
        total_spent = sum([expense.amount for expense in self.expenses if expense.user == user])
        print(f"Total expenses by {user}: {total_spent}")

# Testing

tracker = ExpenseTracker()

tracker.set_budget('Food', 'Alhaan', 500)

tracker.add_expense('Food', 50, 'Alhaan')

tracker.view_summary()

tracker.track_by_user('Alhaan')
