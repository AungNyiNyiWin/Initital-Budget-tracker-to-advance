income = 0
expenses = []

while True:
    print("\n=====budget tracker=====")
    print("1. add income:")
    print("2. add expense:")
    print("3. show expense record.")
    print("4. total expense:")
    print("5. remaining balance:")
    print("6. max/min expense:")
    print("7. delete expense:")
    print("8. edit expense amount:")
    print("9. edit category and amount:")
    print("10. exit")

    choice = input("enter choice:")

    if choice == "1":
        while True:
            try:
                new_income = int(input("enter new income:"))
                if new_income <= 0:
                    print("invalid income.")
                else:
                    income += new_income
                    print("income saved.")
                    break
            except ValueError:
                print("please enter number only.")
    elif choice == "2":    
        category = input("enter category: ").strip().lower()
        while True:
            try:
                amount = int(input("enter amount :"))
                if amount <= 0:
                    print("invalid amount.")
                else:
                    expense = {
                        "category":category,"amount":amount
                    }
                    expenses.append(expense)
                    print("expense saved.")
                    break
            except ValueError:
                print("please enter number only.")
    elif choice == "3":
        if not expenses:
            print("no expense recorded.")
        else:
            for expense in expenses:
                print("expense record :",expense["category"],":",expense["amount"])
    elif choice == "4":
        if not expenses:
            print("no expense recorded.")
        else:
            total_expense = sum (expense["amount"]for expense in expenses)
            print("total_expense :",total_expense)
    elif choice == "5":
        if not expenses:
            print("no expense recorded.")
        else:
            total_expense = sum (expense["amount"]for expense in expenses)
            remaining_balance = income-total_expense
            print("remaining balance :",remaining_balance)
    elif choice == "6":
        if not expenses:
            print("no expense recorded.")
        else:
            max_expense = max(expenses,key= lambda expense:expense["amount"])
            min_expense = min(expenses,key=lambda expense:expense["amount"])
            print("maximum expense:",max_expense["category"],":",max_expense["amount"])
            print("manimum expense:",min_expense["category"],":",min_expense["amount"])
    elif choice == "7":
        if not expenses:
            print("no expense recorded.")
        else:
            for i,expense in enumerate(expenses,start=1):
                print(i,expense["category"],":",expense["amount"])
        try:
            delete_number = int(input("enter expense number to delete :"))
            expenses.pop(delete_number-1)
            print("expense deleted.")
            for expense in expenses:
                print(expense["category"],":",expense["amount"])
        except ValueError:
            print("please enter number only.")
        except IndexError:
            print("invalid number .")
    elif choice == "8":
        if not expenses:
            print("no expense recorded.")
        else:
            for i,expense in enumerate(expenses,start=1):
                print(i,expense["category"],":",expense["amount"])
        try:
            edit_number = int(input("enter expense number to edit :"))
            new_amount = int(input("enter new amount:"))
            if new_amount <= 0:
                print("invalid new amount")
            else:

                expenses[edit_number-1]["amount"]=new_amount
                print("expense editted.")
                for expense in expenses:
                    print(expense["category"],":",expense["amount"])
        except ValueError:
            print("please enter number only.")
        except IndexError:
            print("invalid number .")
    elif choice == "8":
        if not expenses:
            print("no expense recorded.")
        else:
            for i,expense in enumerate(expenses,start=1):
                print(i,expense["category"],":",expense["amount"])
        try:
            edit_number = int(input("enter expense number to edit :"))
            new_category = input("enter new category:")
            expenses[edit_number-1]["category"]=new_category
            new_amount = int(input("enter new amount:"))
            if new_amount <= 0:
                print("invalid new amount.")
            else:

                expenses[edit_number-1]["amount"]=new_amount
                print("expense editted.")
                for expense in expenses:
                    print(expense["category"],":",expense["amount"])
        except ValueError:
            print("please enter number only.")
        except IndexError:
            print("invalid number .")
    elif choice == "10":
        print("exit.")
        break
    





               


        