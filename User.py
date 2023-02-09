class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
        
    
    def describe_user(self):
        "describing user"
        print("----------------------")
        print(f"Name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"User age: {self.age}")
        print("----------------------")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")
        print("----------------------")

    def increment_login_attempts(self):
        """increments the value of login_attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """that resets the value of login_attempts to 0"""
        self.login_attempts = 0

class Admin(User):
    """An administrator is a special kind of user."""
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        #se necesita iniciar con un set de privilegios vacios
        #llamar a clase hijo Privileges
        self.privileges = Privileges()


class Privileges():
    """Mostrará los privilegios"""
    def __init__(self, privileges = []):
        self.privileges = privileges


    def show_privileges(self):
        """Muestra los privilegios del admin"""
        print(f"Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"this user has no privileges!")

# profile = User("Melissa", "Fararoni", 29)
# profile.describe_user()
# profile.greet_user()

# user = User("Gian", "Fararoni", 1)
# user.describe_user()
# user.greet_user()

# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(f"User: {user.first_name} {user.last_name} try to login: {user.login_attempts} times")

# user.reset_login_attempts()
# print(f"User: {user.first_name} {user.last_name} try to login: {user.login_attempts} times")

meli = Admin("Melissa", "Fararoni", 29)
meli.describe_user()

meli.privileges.show_privileges()

print(f"Adding privileges...")
meli.privileges.privileges = [
    "can add post" ,
    "can delete post" , 
    "can ban user"
]

meli.privileges.show_privileges()


