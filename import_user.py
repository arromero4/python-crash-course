from User import User, Admin, Privileges

meli = Admin("Melissa", "Fararoni", 29)
meli.describe_user()



print(f"Adding privileges...")
meli.privileges.privileges = [
    "can add post" ,
    "can delete post" , 
    "can ban user"
]

meli.privileges.show_privileges()