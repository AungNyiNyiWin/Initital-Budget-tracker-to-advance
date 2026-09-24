from income import save_income,total_income
from expense import save_expense,total_expense

def income_menu():
    while True:
        print("===Budget Tracker===")
        print("1. save income")
        print("3. delete incomes")
        print("4. edit income amount")
        print("5. edit income source")
        print("6. edit income note")
        print("7. back")

        choice = input("enter choice:")
        if choice == "1":
            save_income()
        elif choice == "2":
            income = total_income()
            print("total income:",income)
        elif choice == "3":
            print("exit")
            break
        else:
             print("invalid income")

def expense_menu():
    while True:
        print("====expense menu====")
        print("1. save expense")
        print("2. delete expense ")
        print("3. edit expense amount")
        print("4. edit expense category")
        print("5. edit expense note")
        print("6. back")

        expense_choice = input("enter choice:")
        if expense_choice == "1":
            save_expense()
        elif expense_choice == "2":
            expense = total_expense()
            print("total expense:",expense)