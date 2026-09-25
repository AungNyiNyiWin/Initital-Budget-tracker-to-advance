


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

def get_text(message):
    return input(message)