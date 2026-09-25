def get_positive_number (message):
    while True:
        try:
            number = int(input(message))
            if number <= 0 :
                print("enter positive number only")
            else:
                return number
        except ValueError:
            print("enter number only no text.")

def show_list(items, key_name):
    for i,item in enumerate(items,start=1):
        print(i,item[key_name],":",item["amount"],":",item["date"],":",item["note"])

def remaining_balance (income,expense):
    balance = income - expense
    return balance

def delete_number(items,get_number):
    index = get_number(items)
    items.pop(index)

def update_items(items,get_number,key,get_value):
    index = get_number(items)
    value = get_value()
    items[index][key]= value

def get_amount():
    return get_positive_number("enter amount:")

def get_text(message):
    return input(message)


