expenses = []
from datetime import date

def save_expense():
    category = input("enter category:").strip().lower()
    amount = int(input("enter amount"))
    today = date.today()
    dmy_date = today.strftime("%d-%m-%Y")
    note = input("enter note:").strip().lower()
    expense = {
        "category":category,"amount":amount,"date":dmy_date,"note":note
    }
    expenses.append(expense)
    print("expense saved.")

def total_expense():
    if not expenses:
        return 0
    else:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        return total

    
    