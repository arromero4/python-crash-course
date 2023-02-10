from car import Car, ElectricCar

vocho = Car('volkswagen', 'vocho', 2019)
print(vocho.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

import car
vocho = car.Car('volkswagen', 'vocho', 2019)
print(vocho.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())