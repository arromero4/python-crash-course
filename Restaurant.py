class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describing restaurant"""
        print(f"Name of the restaurant: {self.restaurant_name}")
        print(f"Type of restaurant cuisine: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Opening the restaurant"""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self,number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served
    
    def increment_number_served(self, number_served):
        """Allow user to increment the number of customers served."""
        self.number_served += number_served

class IceCreamStand(Restaurant):
    """Inherits from Restaurant"""
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def ice_Cream_Flavors(self):
        print(f"Hay estos sabores de helado: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


#Creo una instancia de IceCreamStand
#no le paso el tipo de restaurante porque ya está por default para los helados
#le paso una lista de sabores al atributo flavors
icecream = IceCreamStand('the gelatto king')
icecream.flavors = ['chocolate', 'vanilla','strawberry']

#con la herencia llamo al metodo que describe el restaurante
#y llamo al metodo de la clase hijo 
icecream.describe_restaurant()
icecream.ice_Cream_Flavors()

# restaurant_1 = Restaurant("Liru Cisar", "Italian food")
# restaurant_2 = Restaurant("Taquearte", "Mexican food")
# restaurant_3 = Restaurant("Ratatouille", "French food")

# restaurant_1.describe_restaurant()
# restaurant_1.open_restaurant()

# restaurant_2.describe_restaurant()
# restaurant_2.open_restaurant()

# restaurant_3.describe_restaurant()
# restaurant_3.open_restaurant()

# restaurant = Restaurant('the mean queen', 'pizza')
# restaurant.describe_restaurant()


# restaurant.number_served = 430
# print(f"Number served: {restaurant.number_served}")

# restaurant.set_number_served(500)
# print(f"Number that has been served: {restaurant.number_served}")

# restaurant.increment_number_served(100)
# print(f"Number served has incremented to: {restaurant.number_served}")