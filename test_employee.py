import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self) :
        """Use the setUp()
method so you don’t have to create a new employee instance in each test method."""
        #create instance of Employee
        self.checo = Employee('sergio','perez', 35000)
    
    def test_give_default_raise(self):
        """adds $5,000 to the annual salary by default"""
        self.checo.give_raise()
        self.assertEqual(self.checo.salary, 40000)

    def test_give_custom_raise(self):
        """adds custom annual salary """
        self.checo.give_raise(10000)

        self.assertEqual(self.checo.salary, 45000)
    

if __name__ == '__main__':
    unittest.main()