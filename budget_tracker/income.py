incomes = []
from datetime import date
from report import get_positive_number,delete_number,show_list,update_items,get_amount,get_text

def add_income():
    source = input("enter source:").strip().lower()
    amount = get_positive_number("enter income amount:")
    today = date.today()
    dmy_date = today.strftime("%d-%m-%Y")
    note = input("enter note:").strip().lower()
    income = {
        "source":source,"amount":amount,"date":dmy_date,"note":note
    }
    incomes.append(income)
    print("income saved.")

def total_income():
    if not incomes:
        return 0
    else:
        total = 0
        for income in incomes:
            total += income["amount"]
        return total

def get_income_number(incomes):
    number = int(input("enter income number:"))
    if number <1 or number> len(incomes):
        raise IndexError
    return number -1

def max_min_income():
    if not incomes:
        return None
    else:
        max_income = max(incomes , key= lambda income:income["amount"])
        min_income = min(incomes , key= lambda income:income["amount"])
    return max_income,min_income

def show_maxmin_income():
    result = max_min_income()
    if result is None:
        print("no income saved.")
    else:
        max_income,min_income = result
        print(max_income["source"],":",max_income["amount"],":",max_income["date"],":",max_income["note"])
        print(min_income["source"],":",min_income["amount"],":",min_income["date"],":",min_income["note"])

def total_income_summary():
    if not incomes:
        print("no income recorded.")
    else:
        income_total = {}
        for income in incomes:
            source = income["source"]
            amount = income["amount"]
            if source not in income_total:
                income_total[source]= 0
            income_total[source]+= amount
        return income_total

def total_income_source_bysearch(incomes,source):
    if not incomes:
        return None
    else:
        total = 0
        for income in incomes:
            if income["source"]== source:
                total += income["amount"]
            return total

def show_total_income_source_bysearch():
    source = input("enter source:").stip().lower()
    income_result = total_income_source_bysearch(incomes,source)
    if income_result is None:
        print("no income recorded.")
    else:
        print("total income source by search :",income_result)

def delete_income():
    if not incomes:
        print("no incomes saved.")
    else:
        show_list(incomes,"source")
        try:
            delete_number(incomes,get_income_number)
            print("income deleted.")
            show_list(incomes,"source")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter income number only")

def edit_income_amount():
    if not incomes:
        print("no incomes saved.")
    else:
        show_list(incomes,"source")
        try:
            update_items(incomes,get_income_number,"amount",get_amount)
            print("income amount edited.")
            show_list(incomes, "source")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter income number only")  


def edit_income_source():
    if not incomes:
        print("no incomes saved.")
    else:
        show_list(incomes,"source")
        try:
            update_items(incomes,get_income_number,"source",lambda :get_text("enter new source:"))
            print("income source edited.")
            show_list(incomes, "source")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter income number only")  

def edit_income_note():
    if not incomes:
        print("no incomes saved.")
    else:
        show_list(incomes,"source")
        try:
            update_items(incomes,get_income_number,"note",lambda :get_text("enter new note:"))
            print("income note edited.")
            show_list(incomes, "source")
        except ValueError:
            print("please enter number only no text.")
        except IndexError:
            print("please enter income number only") 

def show_income_list():
    if not incomes:
        print("no incomes saved.")
    else:
        show_list(incomes,"source")

