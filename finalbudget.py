income = 0
expenses = []

def save_income():
    global income
    while True:
        try:
            new_income = int(input("enter new income:"))
            if new_income<=0:
                print("invalid income.")
            else:
                income += new_income
                print("income saved.")
                break
        except ValueError:
            print("please enter number only.")

def save_expense():
    category = input("enter category").strip().lower()
    while True:
        try:
            amount = int(input("enter amount"))
            if amount <= 0:
                print("invalid amount")
            else:
                expense={
                    "category":category,"amount":amount
                }
                expenses.append(expense)
                print("expense saved.")
                break
        except ValueError:
            print("please enter number only")

def expense_record():
    if not expenses:
        print("no expense recorded.")
    else:
        for expense in expenses:
            print("expense record :",expense["category"],":",expense["amount"])

def total_expense(expenses):
    if not expenses:
        return 0
    else:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        return total

def remaining_balance(income,expenses):
    if not expenses:
        return 0
    else:
        total = total_expense(expenses)
        balance = income - total
    return balance

def max_min_expense(expenses):
    if not expenses:
        return None
    else:
        max_expense = max(expenses,key=lambda expense:expense["amount"])
        min_expense = min(expenses,key=lambda expense:expense["amount"])
    return max_expense,min_expense

def show_expense_list(expenses):
    for i,expense in enumerate(expenses,start=1):
        print(i,expense["category"],":",expense["amount"])

def get_expense_number(expenses):
    show_expense_list(expenses)
    number = int(input("enter expense number:"))
    if number < 1 or number > len(expenses):
        raise IndexError   #အသစ်နေရာ
    return number -1

def delete_expense():
    if not expenses:
        print("no expense recorded.")
    else:
        try:
            index = get_expense_number(expenses)
            expenses.pop(index)
            print("expense deleted")
            show_expense_list(expenses)
        except ValueError:
            print("please enter number only")
        except IndexError:
            print("please enter expense number only")

def edit_amount():
    if not expenses:
        print("no expense recorded.")
    else:
        try:
            index = get_expense_number(expenses)
            new_amount = int(input("enter new amount:"))
            expenses[index]["amount"]=new_amount
            print("expense's amount edited.")
            show_expense_list(expenses)
        except ValueError:
            print("please enter number only")
        except IndexError:
            print("please enter expense number only")

def edit_amount_category():
    if not expenses:
        print("no expense recorded.")
    else:
        try:
            index = get_expense_number(expenses)
            new_category = input("enter new category").strip().lower()
            new_amount = int(input("enter new amount:"))
            expenses[index]["category"]=new_category
            expenses[index]["amount"]=new_amount
            print("expense's amount edited.")
            show_expense_list(expenses)
        except ValueError:
            print("please enter number only")
        except IndexError:
            print("please enter expense number only")

while True:
    print("===budget tracker===")
    print("1. add income")
    print("2. add expense")
    print("3. expense record.")
    print("4. total expense.")
    print("5. remaining balance")
    print("6. max/min expense")
    print("7. delete expense")
    print("8. edit amount")
    print("9. edit category and amount")
    print("10. exit")
    choice = input("enter choice:")

    if choice == "1":
        save_income()
    elif choice == "2":
        save_expense()
    elif choice == "3":
        expense_record()
    elif choice == "4":
        print("total expense:",total_expense(expenses))
    elif choice == "5":
        print("remaining balance:",remaining_balance(income,expenses))
    elif choice == "6":
        result = max_min_expense(expenses)
        if result is None:
            print("no expense recorded.")
        else:
            max_expense,min_expense = result
            print(max_expense["category"],":",max_expense["amount"])
            print(min_expense["category"],":",min_expense["amount"])
    elif choice== "7":
        delete_expense()
    elif choice=="8":
        edit_amount()
    elif choice=="9":
        edit_amount_category()
    elif choice =="10":
        print("Exit")
        break
    else:
        print("invalid choice.")

