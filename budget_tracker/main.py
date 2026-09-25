from income import add_income,delete_income,edit_income_amount,edit_income_source,edit_income_note,total_income,total_income_summary,show_total_income_source_bysearch,show_maxmin_income,show_income_list

from expense import save_expense,delete_expense,edit_expense_amount,edit_expense_category,edit_expense_note,total_expense,total_expense_summary,show_total_expense_category_bysearch,show_maxmin_expense,show_expense_list

from report import remaining_balance

def income_menu():
    while True:
        print("1. add income.")
        print("2. delete income")
        print("3. edit income amount")
        print("4. edit income source")
        print("5. edit income note")
        print("6. back")

        income_choice = input("enter income choice:")
        if income_choice == "1":
            add_income()
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
            print("invalid income choice.")


def expense_menu():
    while True:
        print("1. add expense")
        print("2. delete expense")
        print("3. edit expense amount")
        print("4. edit expense category")
        print("5. edit expense note")
        print("6. back")

        expense_choice = input("enter expense choice:")
        if expense_choice == "1":
            save_expense()
        elif expense_choice == "2":
            delete_expense()
        elif expense_choice =="3":
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
        print("1. total income")
        print("2. total expense")
        print("3. total income summary")
        print("4. total expense summary")
        print("5. total income source by search ")
        print("6. total expense category by search")
        print("7. max_min_income")
        print("8. max_min_expense")
        print("9. remaining balance")
        print("10. expense record")
        print("11. income record")
        print("12. back")

        report_choice = input("enter report choice:")
        if report_choice == "1":
            print("total income:",total_income())
        elif report_choice == "2":
            print("total expense:",total_expense())
        elif report_choice == "3":
            income_total= total_income_summary()
            print(income_total)
        elif report_choice == "4":
            expense_total = total_expense_summary()
            print(expense_total)
        elif report_choice == "5":
            show_total_income_source_bysearch()
        elif report_choice == "6":
            show_total_expense_category_bysearch()

        elif report_choice == "7":
            print(show_maxmin_income())
        elif report_choice == "8":
            print(show_maxmin_expense())
        elif report_choice == "9":
            income = total_income()
            expense = total_expense()
            result = remaining_balance(income,expense)
            print("remaining balace",result)
        elif report_choice == "10":
            print(show_income_list())
        elif report_choice == "11":
            print(show_expense_list())
        elif report_choice == "12":
            print("back")
            break
        else:
            print("invalid report choice.")
        
while True:
    print("======Budget Tracker =====")
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
        print("exit")
        break
    else:
        print("invalid choice.")
            
        
        
        
        

        


