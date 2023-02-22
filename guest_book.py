filename = "guest_book.txt"

while True:
    name = input("\nPlease enter your name: ")
    print("(enter 'q' at any time to quit)")

    if name == 'q':
        break

    with open(filename, 'a') as file_object:
        file_object.write(f"Hello {name}, thank you for visiting us!\n")

    print(f"Hello {name}, thank you for visiting us!")



