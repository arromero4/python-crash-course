import json

def favorite_number():
    """input the name and then save the number in json"""

    user = input("Enter your name: ")
    filename = 'favorite_number.json'

    try:
        with open(filename) as f:
            number = json.load(f)

    except FileNotFoundError:
        number = input("What is your favorite number? ")
        with open(filename, 'w') as f:
            json.dump(number, f)
        print("Thanks, I'll remember that.")
    else:
        print(f"I know your favorite number! It's {number}.")
favorite_number()