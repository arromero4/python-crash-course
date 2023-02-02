class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
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


profile = User("Melissa", "Fararoni", 29)
profile.describe_user()
profile.greet_user()

profile2 = User("Gian", "Fararoni", 1)
profile2.describe_user()
profile2.greet_user()

