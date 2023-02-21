filename = "guest.txt"
guest = input("Please enter your name: ")

with open(filename,'w') as file_object:
    file_object.write(guest)

