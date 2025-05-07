
import csv
import os

expenses = []
monthly_budget = 0

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    description = input("Enter a brief description: ")
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded.")
        return
    for idx, expense in enumerate(expenses, start=1):
        if all(k in expense for k in ['date', 'category', 'amount', 'description']):
            print(f"{idx}. {expense['date']} | {expense['category']} | ₹{expense['amount']} | {expense['description']}")
        else:
            print(f"{idx}. Incomplete expense entry. Skipped.")

def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to ₹{monthly_budget}")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def track_budget():
    total_expense = sum(exp['amount'] for exp in expenses)
    print(f"\n--- Budget Tracker ---")
    print(f"Total spent: ₹{total_expense}")
    print(f"Monthly Budget: ₹{monthly_budget}")
    if total_expense > monthly_budget:
        print("⚠️ You have exceeded your budget!")
    else:
        print(f"✅ You have ₹{monthly_budget - total_expense} left for the month.")

def save_expenses(filename='expenses.csv'):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print("Expenses saved successfully.")

def load_expenses(filename='expenses.csv'):
    if not os.path.exists(filename):
        return
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row['amount'] = float(row['amount'])
                expenses.append(row)
            except ValueError:
                continue

def menu():
    load_expenses()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Exiting... Expenses saved.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")

menu()
