income = 0
expenses = []
def add_income():
    global income

    while True:
        try:
            new_income = int(input("enter new income"))
            if new_income <= 0:
                print("invalid new income.")
            else:
                income += new_income
                print("income saved.")
                break
        except ValueError:
            print("please enter a number")


def add_expense():
    category = input("enter category:").strip().lower()
    while True:
        try:
            amount = int(input("enter amount:"))
            if amount <= 0:
                print("invalid amount")
            else:
                expense = {
                    "category":category,"amount":amount
                }
                expenses.append(expense)
                print("expense saved.")
                break
        except ValueError:
            print("please enter a number")

def show_expense():
    if not expenses:
        print("no expense recorded.")
    else:
        for expense in expenses:
            print(expense["category"],":",expense["amount"])

def total_expense(expenses):
    if not expenses:
        return 0
    else:
        total = 0
        for expense in expenses:
            total += expense["amount"]  # လောလောဆယ်ဒီနားပြောင်းသွားပါပြီ။ total မူလတန်ဖိုး ၀ ပါ။ total ထဲကို expense amount တွေ ထည့်ပေါင်းတဲ့ပုံစံပါ။
        return total

def remaining_balance(income,expenses):
    if not expenses:
        return 0
    else:
        total = total_expense(expenses)
        balance = income-total
    return balance

def max_min_expense(expenses):
    if not expenses:
        return None
    else:
        max_expense = max(expenses,key=lambda expense:expense["amount"])
        min_expense = min(expenses,key=lambda expense:expense["amount"])
    return max_expense,min_expense

def delete_expense():
    if not expenses:
        print("no expense recorded.")
    else:
        for i,expense in enumerate(expenses,start=1):
            print(i,expense["category"],":",expense["amount"])
        try:
            delete_number = int(input("enter expense number to delete:"))
            expenses.pop(delete_number-1)
            print("expense deleted.")
            for expense in expenses:
                print(expense["category"],":",expense["amount"])
        except ValueError:
            print("enter number only no text.")
        except IndexError:
            print("enter correct expense number.")

def edit_amount():
    if not expenses:
        print("no expense recorded.")
    else:
        for i,expense in enumerate(expenses,start=1):
            print(i,expense["category"],":",expense["amount"])
        try:
            edit_number = int(input("enter expense number to edit:"))
            new_amount = int(input("enter new amount:"))
            if new_amount <= 0:
                print("invalid new amount.")
            else:
                expenses[edit_number-1]["amount"]=new_amount
                print("expense edited.")
                for expense in expenses:
                    print(expense["category"],":",expense["amount"])
        except ValueError:
            print("enter number only no text.")
        except IndexError:
            print("enter correct expense number.") 

def edit_amount_category():
    if not expenses:
        print("no expense recorded.")
    else:
        for i,expense in enumerate(expenses,start=1):
            print(i,expense["category"],":",expense["amount"])
        try:        
            edit_number = int(input("enter expense number to edit:"))
            new_category= input("enter new category").strip().lower()
            expenses[edit_number-1]["category"]=new_category
            new_amount = int(input("enter new amount:"))
            if new_amount <= 0:
                print("invalid new amount.")
            else:
                expenses[edit_number-1]["amount"]=new_amount
                print("category and amount edited.")
                for expense in expenses:
                    print(expense["category"],":",expense["amount"])
        except ValueError:
            print("enter number only no text.")
        except IndexError:
             print("enter correct expense number.")





while True:
    print("1. add income:")
    print("2. add expense.")
    print("3. show expense record.")
    print("4. total expense")
    print("5. remaining balance")
    print("6. max/min expense")
    print("7. delete expense")
    print("8. edit amount")
    print("9. edit category and amount.")
    print("10. exit")
    choice = input("enter choice")
    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice =="3":
        show_expense()
    elif choice == "4":
        print("total expense:",total_expense(expenses))
    elif choice == "5":
        print("remaining balance:",remaining_balance(income,expenses))  #return function အရ ဒီလိုရေးပေးရပါတယ်။
    elif choice == "6":
        result = max_min_expense(expenses)
        if result is None:
            print("no income saved.")
        else:
            max_expense,min_expense = result
            print("max expense :", max_expense["category"],":",max_expense["amount"])
            print("min expense :", min_expense["category"],":",min_expense["amount"])
    elif choice == "7":
        delete_expense()
    elif choice == "8":
        edit_amount()
    elif choice == "9":
        edit_amount_category()
    elif choice == "10":
        print("good bye")
        break
    else:
        print("invalid input.")