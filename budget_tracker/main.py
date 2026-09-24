from income import save_income,total_income,total_income_summary,show_max_min_income,show_income_source_total_bysearch,edit_income_amount,edit_income_note,edit_income_source,delete_income
from expense import save_expense,total_expense,total_expense_summary,show_max_min_expense,show_expense_category_bysearch,edit_expense_amount,edit_expense_category,edit_expense_note,delete_expense
from report import remaining_balance
def income_menu():
    while True:
        print("===Budget Tracker===")
        print("1. save income")
        print("2. delete incomes")
        print("3. edit income amount")
        print("4. edit income source")
        print("5. edit income note")
        print("6. back")

        income_choice = input("enter choice:")
        if income_choice == "1":
            save_income()
        elif income_choice == "2":
            delete_income()
        elif income_choice == "3":
            edit_income_amount()
        elif income_choice == "4":
            edit_income_source()
        elif income_choice == "5":
            edit_income_note()
        elif income_choice == "6":
            print("back")
            break
        else:
             print("invalid income choice")

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
            delete_expense()
        elif expense_choice == "3":
            edit_expense_amount()
        elif expense_choice == "4":
            edit_expense_category()
        elif expense_choice == "5":
            edit_expense_note()
        elif expense_choice == "6":
            print("back")
            break
        else:
            print("invalid expense choice.")

def reports():
    while True:
        print("\n====reports====")
        print("1. total income:")
        print("2. total expense:")
        print("3. total income summary")
        print("4. total expense summary")
        print("5. max/min income")
        print("6. max/min expense")
        print("7. income total  source by search")
        print("8. expense total category by search")
        print("9. remaining balance.")
        print("10. back")

        report_choice = input("enter report choice:")
        if report_choice == "1":
            income = total_income()
            print("total income:",income)
        elif report_choice == "2":
            expense =total_expense()
            print("total expense:",expense)
        elif report_choice == "3":
            total_income_summary()
        elif report_choice == "4":
            total_expense_summary()
        elif report_choice == "5":
            show_max_min_income()
        elif report_choice == "6":
            show_max_min_expense()
        elif report_choice == "7":
            show_income_source_total_bysearch()
        elif report_choice == "8":
            show_expense_category_bysearch()
        elif report_choice == "9":
            income_total = total_income()
            expense_total = total_expense()
            balance = remaining_balance(income_total,expense_total)
            print("remaining balance:",balance)
        elif report_choice == "10":
            print("back")
            break
        else:
            print("invalid report choice.")

while True:
    print("====budget tracker====")
    print("1. income menu")
    print("2. expense menu")
    print("3. reports")
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
        print("invalid choice")




        


