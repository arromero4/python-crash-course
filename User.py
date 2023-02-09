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
    

profile = User("Melissa", "Fararoni", 29)
profile.describe_user()
profile.greet_user()

user = User("Gian", "Fararoni", 1)
user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"User: {user.first_name} {user.last_name} try to login: {user.login_attempts} times")

user.reset_login_attempts()
print(f"User: {user.first_name} {user.last_name} try to login: {user.login_attempts} times")


