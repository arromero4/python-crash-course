question = "Please enter your age: "
question += "\nEnter '0' when you are finished."

while True:
    ticket = int(input(question))

    if ticket < 3:
        print("the ticket is free")
    elif ticket < 12:
        print("the ticket is $10")
    else:
        print("the ticket is $15") 
    
    if ticket == 0:
        break