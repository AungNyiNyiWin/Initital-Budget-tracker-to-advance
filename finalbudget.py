incomes = []
expenses = []
from datetime import date

def get_positive_number(message):
    while True:
        try:
            number = int(input(message))
            if number <= 0:
                print("please enter positive number ")
            else:
                return number
        except ValueError:
            print("please enter number only.")

def save_income():
    source = input("enter source:").strip().lower()
    amount = int(input("enter amount:"))
    today = date.today()
    dmy_date = today.strftime("%d-%m-%Y")
    note = input("enter note").strip().lower()
    income = {
        "source":source,"amount":amount,"date":dmy_date,"note":note
    }
    incomes.append(income)
    print("income saved.")

def save_expense():
    category = input("enter category:").strip().lower()
    amount = int(input("enter amount:"))
    today = date.today()
    dmy_date=today.strftime("%d-%m-%Y")
    note = input("enter note:").strip().lower()
    expense = {
        "category":category,"amount":amount,"date":dmy_date,"note":note
    }
    expenses.append(expense)
    print("expense saved.")

def total_expense(expenses):
    if not expenses:
        return 0
    else:
        total= 0
        for expense in expenses:
            total += expense["amount"]
        return total

def total_income(incomes):
    if not incomes:
        return 0
    else:
        total = 0
        for income in incomes:
            total += income["amount"]
        return total

def remaining_balance (incomes,expenses):
    income = total_income(incomes)
    expense =total_expense(expenses)
    balance = income - expense
    return balance

def total_expense_summary(expenses):
    if not expenses:
        return 0
    else:
        expense_total = {}
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category not in expense_total:
                expense_total[category]= 0
            expense_total[category]+= amount
        return expense_total

def total_income_summary(incomes):
    if not incomes:
        return 0
    else:
        income_total = {}
        for income in incomes:
            source = income["source"]
            amount = income["amount"]
            if source not in income_total:
                income_total[source]=0
            income_total[source]+= amount
        return income_total

def show_list(items,name_key):
    for i,item in enumerate(items,start=1):
        print(i,item[name_key],":",item["amount"],":",item["date"],":",item["note"])

def delete_number(items,get_number):
    index = get_number(items)
    items.pop(index)

def update_item(items,get_number,key,get_value):
    index = get_number(items)
    Value = get_value()  #import parenthesis ()
    items[index][key] = Value

def get_expense_number(expenses):
    number = int(input("enter expense number:"))
    if number <1 or number > len(expenses):
        raise IndexError
    return number -1

def get_income_number(incomes):
    number = int(input("enter income number:"))
    if number <1 or number> len(incomes):
        raise IndexError
    return number -1

def get_amount():
    return get_positive_number("enter amount:")

def get_text(message):
    return input(message)

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
            print("please enter number only no text.")
        except IndexError:
            print("please enter expense number only .")

def delete_income():
    if not incomes:
        print("no incomes added.")
    else:
        show_list(incomes,"source")
        try:
            delete_number(incomes,get_income_number)
            print("income deleted.")
            show_list(incomes,"source")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter income number only .")

def edit_expense_amount():
    if not expenses:
        print("no expense recorded.")
    else:
        show_list(expenses,"category")
        try:
            update_item(expenses,get_expense_number,"amount",get_amount)
            print("expense amount edited.")
            show_list(expenses,"category")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter expense number only .")

def edit_income_amount():
    if not incomes:
        print("no incomes saved.")
    else:
        show_list(incomes,"source")
        try:
            update_item(incomes,get_income_number,"amount",get_amount)
            print("income amount edited.")
            show_list(incomes,"source")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter income number only .")

def edit_expense_category():
    if not expenses:
        print("no expense recorded.")
    else:
        show_list(expenses,"category")
        try:
            update_item(expenses,get_expense_number,"category",lambda :get_text("enter new category:"))
            print("expense category edited.")
            show_list(expenses,"category")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter expense number only .")

def edit_income_source():
    if not incomes:
        print("no incomes saved.")
    else:
        show_list(incomes,"source")
        try:
            update_item(incomes,get_income_number,"source",lambda: get_text("enter new source:"))
            print("income source edited.")
            show_list(incomes,"source")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter income number only .")

def edit_expense_note():
    if not expenses:
        print("no expense recorded.")
    else:
        show_list(expenses,"category")
        try:
            update_item(expenses,get_expense_number,"note",lambda :get_text("enter new note:"))
            print("expense note edited.")
            show_list(expenses,"category")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter expense number only .")

def edit_income_note():
    if not incomes:
        print("no incomes saved.")
    else:
        show_list(incomes,"source")
        try:
            update_item(incomes,get_income_number,"note",lambda: get_text("enter new note:"))
            print("income note edited.")
            show_list(incomes,"source")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter income number only .")

def max_min_income(incomes):
    if not incomes:
        return None
    else:
        max_income = max(incomes, key= lambda income:income["amount"])
        min_income = min(incomes, key= lambda income:income["amount"])
    return max_income,min_income

def max_min_expense(expenses):
    if not expenses:
        return None
    else:
        max_expense = max(expenses, key=lambda expense:expense["amount"])
        min_expense = min(expenses, key=lambda expense:expense["amount"])
    return max_expense,min_expense

def income_menu():
    while True:
        print("\n===income menu===")
        print("1. save_income")
        print("2. income record")
        print("3. delete income")
        print("4. edit income amount")
        print("5. edit income category")
        print("6. edit income note")
        print("7. Back")
        income_choice = input("enter income choice:")
        if income_choice =="1":
            save_income()
        elif income_choice == "2":
            show_list(incomes,"source")
        elif income_choice == "3":
            delete_income()
        elif income_choice == "4":
            edit_income_amount()
        elif income_choice == "5":
            edit_income_source()
        elif income_choice == "6":
            edit_income_note()
        elif income_choice == "7":
            print("Back")
            break
        else:
            print("invalid income choice.")

def expense_menu():
    while True:
        print("\n===expense menu===")
        print("1. save_expense")
        print("2. expense record")
        print("3. delete expense")
        print("4. edit expense amount")
        print("5. edit expense category")
        print("6. edit expense note")
        print("7. Back")
        expense_choice = input("enter expense choice:")
        if expense_choice == "1":
            save_expense()
        elif expense_choice == "2":
            show_list(expenses,"category")
        elif expense_choice == "3":
            delete_expense()
        elif expense_choice == "4":
            edit_expense_amount()
        elif expense_choice == "5":
            edit_expense_category()
        elif expense_choice == "6":
            edit_expense_note()
        elif expense_choice == "7":
            print("Back")
            break
        else:
            print("invalid expense choice.")

def reports():
    while True:
        print("\n=====reports=====")
        print("1.max/min expenses")
        print("2.max/min incomes")
        print("3.expense summary")
        print("4.income summary")
        print("5.total expense")
        print("6.total income")
        print("7. back")
        reports_choice = input("enter report choice:")
        if reports_choice == "1":
            result = max_min_expense(expenses)
            if result is None:
                print("no expense recorded.")
            else:
                max_expense,min_expense = result
                print(max_expense["category"],":",max_expense["amount"],":",max_expense["date"],":",max_expense["note"])
                print(min_expense["category"],":",min_expense["amount"],":",min_expense["date"],":",min_expense["note"])

        elif reports_choice == "2":
            result = max_min_income(incomes)
            if result is None:
                print("no income recorded.")
            else:
                max_income,min_income = result
                print(max_income["source"],":",max_income["amount"],":",max_income["date"],":",max_income["note"])
                print(min_income["source"],":",min_income["amount"],":",min_income["date"],":",min_income["note"])

        elif reports_choice == "3":
            expense_summary = total_expense_summary(expenses)
            print("total expense summary:", expense_summary)
        elif reports_choice == "4":
            income_summary = total_income_summary(incomes)
            print("total income summary:", income_summary)
        elif reports_choice == "5":
            print("total expense:", total_expense(expenses))
        elif reports_choice == "6":
            print("total incomes:", total_income(incomes))
        elif reports_choice == "7":
            print("Back")
            break
        else:
            print("invalid report choice.")

while True:
    print("\n=====budget tracker====")
    print("1. income menu")
    print("2. expense menu")
    print("3. report menu")
    print("4. exit")
    choice = input("enter choice:")
    if choice == "1":
        income_menu()
    elif choice == "2":
        expense_menu()
    elif choice == "3":
        reports()
    elif choice == "4":
        print("Exit")
        break
    else:
        print("invalid choice.")
        

        