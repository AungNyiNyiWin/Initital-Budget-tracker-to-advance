expenses = []
income = 0

while True:
    print("=============Budget Tracker===========")
    print("1. add income:")
    print("2. add expense:")
    print("3. show expense record:")
    print("4. Total Expense:")
    print("5. Remaining Balance:")
    print("6. Min/Max expense:")
    print("7. delete expense:")
    print("8. edit amount:")
    print("9. edit category + amount:")
    print("10. exit")

    choice = input("Enter your choice:")

    if choice == "1":
        
        while True:
            new_income = int(input("enter new income:"))
            if new_income <= 0:
                print("invaild income:")
            else:
                income += new_income
                print("income saved.")
                print("income :", income)
                break

    elif choice == "2":
        category = input("Enter your category:")
        while True:           
            amount = int(input("Enter your amount:"))
        
            if amount <= 0:
                print("invalid amount.")
                                           #ထပ်တိုးထားသောသင်ခန်းစာပါ။amountသည် ၀ထက်ငယ်ပြီးအနှုတ်ကိန်းဖြစ်လျင် သုံးသည့်flow
           
            else:
                break
        expense = {
                "category":category,"amount":amount
            }
        expenses.append(expense)
        print("expense saved.")
                

    elif choice == "3":
        if not expenses:
            print("no expense recorded")
        else:
            for expense in expenses:
                print("expense record:" ,expense["category"],":",expense["amount"])

    elif choice == "4":
        if not expenses:
            print("no expense recorded")
        else:
            total_expense = sum(expense["amount"]for expense in expenses)
            print("Total expense :", total_expense)
        
    elif choice == "5":
        if not expenses:
            print("no expense recorded")
        else:
            total_expense = sum(expense["amount"]for expense in expenses)
            remaining_balance = income - total_expense
            print("remaining balance :",remaining_balance) 
            if remaining_balance > 0:
                print("you still have money.")

            elif remaining_balance == 0:
                print("your balance is zero.")

            else:
                print("you are in debt.")

    elif choice == "6":
        if not expenses:
            print("no expense recorded")
        else:
            max_expense = max(expenses, key=lambda expense:expense["amount"])
            min_expense = min(expenses, key=lambda expense:expense["amount"])

            print("Maximum Expense:", max_expense["category"],":",max_expense["amount"])
            print("Minimum Expense:", min_expense["category"],":",min_expense["amount"])

    elif choice == "7":
        if not expenses:
            print("no expense recorded")
        else:
            for i,expense in enumerate(expenses,start=1):
                print(i,expense["category"],":",expense["amount"])

            delete_number = int(input("enter expense number to delete:"))

            expenses.pop(delete_number-1) 
            print("expense deleted")

            for expense in expenses:
                print(expense["category"],":",expense["amount"])

    elif choice == "8":
        if not expenses:
            print("no expense recorded")
        else:
            for i,expense in enumerate(expenses,start=1):
                print(i,expense["category"],":",expense["amount"])

            edit_number = int(input("enter expense number to edit:"))
            new_amount = int(input("enter new amount"))

            expenses[edit_number-1]["amount"] = new_amount

            print("expense edited")

            for expense in expenses:
                print(expense["category"],":",expense["amount"])

    elif choice == "9":
        if not expenses:
            print("no expense recorded")
        else:
            for i,expense in enumerate(expenses,start=1):
                print(i,expense["category"],":",expense["amount"])
            edit_number = int(input("enter expense number to edit"))
            new_category = input("Enter new category:")
            new_amount = int(input("Enter new amount:"))

            expenses[edit_number-1]["category"]=new_category
            expenses[edit_number-1]["amount"]=new_amount

            print("category and amount updated.")
            for expense in expenses:
                print(expense["category"],":",expense["amount"])

    elif choice =="10":
        print("Good Bye")
        break





         




         
         
         
         
