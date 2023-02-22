filename = "programming_poll.txt"

while True:
    answer = input("\nPlease enter why you like programming: ")
    print("(enter 'q' at any time to quit)")

    if answer == 'q':
        break

    with open(filename, 'a') as file_object:
        file_object.write(f"{answer}\n")

    print(f"You like programming because: {answer}")


