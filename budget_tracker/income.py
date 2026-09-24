incomes = []
from datetime import date

def save_income():
    source = input("enter source:").strip().lower()
    amount = int(input("enter amount:"))
    today= date.today()
    dmy_date = today.strftime("%d-%m-%Y")
    note = input("enter note").strip().lower()
    income = {
        "source":source,"amount":amount,"date":dmy_date,"note":note
    }
    incomes.append(income)
    print("income saved.")

def total_income():
    if not incomes:
        return 0
    else:
        total =0
        for income in incomes:
            total += income["amount"]
    return total