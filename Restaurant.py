class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describing restaurant"""
        print(f"Name of the restaurant: {self.restaurant_name}")
        print(f"Type of restaurant cuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Opening the restaurant"""
        print(f"{self.restaurant_name} is now open!")

restaurant_1 = Restaurant("Liru Cisar", "Italian food")
restaurant_2 = Restaurant("Taquearte", "Mexican food")
restaurant_3 = Restaurant("Ratatouille", "French food")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()





