from report import delete_number,show_list,update_items,get_amount,get_text
from validation import get
from datetime import date
expenses = []

def save_expense():
    category = input("enter category:").strip().lower()
    amount = get_positive_number("enter expense amount:")
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

def get_expense_number(expenses):  #အရေးကြီးသောနေရာ (expenses သည် delete,edit fuction များတွင်ပါသော parameter (items,get number)တွင် get number = get income numberဟုရေးသော်လည်း မူရင်းတွင် incomes ဿို့ expenses ပြမှသာအလုပ်လုပ်မည်ဖြစ်ပါသည်။ )
    number = int(input("enter expense number:"))
    if number < 1 or number > len(expenses):
        raise IndexError
    return number -1

def max_min_expense():
    if not expenses:
        return None
    else:
        max_expense = max(expenses, key=lambda expense:expense["amount"])
        min_expense = min(expenses, key=lambda expense:expense["amount"])
    return max_expense,min_expense

def show_maxmin_expense():
    result = max_min_expense()
    if result is None:
        print("no expense recorded.")
    else:
        max_expense,min_expense = result
        print(max_expense["category"],":",max_expense["amount"],":",max_expense["date"],":",max_expense["note"])
        print(min_expense["category"],":",min_expense["amount"],":",min_expense["date"],":",min_expense["note"])

def total_expense_summary():
    if not expenses:
        print("no expense recorded.")
    else:
        expense_total = {}
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category not in expense_total:
                expense_total[category] = 0
            expense_total[category]+= amount
        return expense_total

def total_expense_category_bysearch(expenses,category):
    if not expenses:
        return None
    else:
        total = 0
        for expense in expenses:
            if expense["category"] == category:
                total += expense["amount"]
            return total

def show_total_expense_category_bysearch():
    category = input("enter category:").strip().lower()
    expense_result = total_expense_category_bysearch(expenses,category)
    if expense_result is None:
        print("no expense recorded.")
    else:
        print("total expense category by search:",expense_result)

def delete_expense():
    if not expenses:
        print("no expense recorded.")
    else:
        show_list(expenses,"category")
        try:
            delete_number(expenses,get_expense_number)
            print("expense deleted.")
            show_list(expenses,"category")
        except ValueError:
            print("please enter number only no text")
        except IndexError:
            print("please enter expense number only")

def edit_expense_amount():
    if not expenses:
        print("no expense recorded.")
    else:
        show_list(expenses,"category")
        try:
            update_items(expenses,get_expense_number,"amount",get_amount)
            print("expense amount edited.")
            show_list(expenses,"category")
        except ValueError:
            print("please enter number only no text")
        except IndexError:
            print("please enter expense number only")

def edit_expense_category():
    if not expenses:
        print("no expense recorded.")
    else:
        show_list(expenses,"category")
        try:
            update_items(expenses,get_expense_number,"category",lambda :get_text("enter new category:"))
            print("expense category edited.")
            show_list(expenses,"category")
        except ValueError:
            print("please enter number only no text")
        except IndexError:
            print("please enter expense number only")

def edit_expense_note():
    if not expenses:
        print("no expense recorded.")
    else:
        show_list(expenses,"category")
        try:
            update_items(expenses,get_expense_number,"note",lambda :get_text("enter new note:"))
            print("expense note edited.")
            show_list(expenses,"category")
        except ValueError:
            print("please enter number only no text")
        except IndexError:
            print("please enter expense number only")

def show_expense_list():
    if not expenses:
        print("no expense recorded.")
    else:
        show_list(expenses,"category")


        




