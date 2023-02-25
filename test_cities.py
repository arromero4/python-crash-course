import unittest
from city_functions import get_formatted_citi

class CitiesTestCase(unittest.TestCase):
    """Test for city_function.py"""
    def test_city_country(self):
        "testing formatted data"""
        formatted_cities = get_formatted_citi('santiago', 'chile')
        self.assertEqual(formatted_cities, 'Santiago, Chile')
        
    def test_city_country_population(self):
        """testing with population as an option"""
        formatted_cities = get_formatted_citi('santiago', 'chile', '5000000')
        self.assertEqual(formatted_cities, 'Santiago, Chile - Population 5000000')
if __name__ == '__main__':
    unittest.main()
