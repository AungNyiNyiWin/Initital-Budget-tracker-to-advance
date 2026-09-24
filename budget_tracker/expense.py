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

def total_expense_summary():
    if not expenses:
        print("no expense recorded.")    
    else:
        expense_total = {}
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category not in expense_total:
                expense_total[category]=0
            expense_total[category]+= amount
        return expense_total

def expense_category_bysearch(expenses,category):
    if not expenses:
        return 0
    else:
        total = 0
        for expense in expenses:
            if expense["category"]== category:
                total += expense["amount"]
        return total

def get_expense_number():
    number = int(input("enter expense number:"))
    if number <1 or number > len(expenses):
        raise IndexError
    return number -1

def delete_expense():
    if not expenses:
        print("no expense recorded.")
    else:




    