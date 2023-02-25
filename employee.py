class Employee:
    """Employee anual salary"""
    def __init__(self, first_name, last_name, salary):
        """The __init__() method should take
in a ﬁrst name, a last name, and an annual salary, and store each of these as attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, amount = 5000):
        """adds $5,000 to the annual salary"""
        self.salary += amount
