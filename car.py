class Car:
    """Representará un carro"""

    def __init__(self, make, model, year):
        """Se inicializan los atributos para el auto"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Regresar la descripción de auto"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Imprime los km que el auto tiene."""
        print(f"Este auto tiene: {self.odometer_reading} KM.")

    def update_odometer(self, kilometers):
        """
        Establece el odometro leyendo el valor dado.
        Rechaza el cambio si se intenta cambiar el odometro
        """
        if kilometers >= self.odometer_reading:
            self.odometer_reading = kilometers
        else:
            print("No puedes regresar un odometro!")

    def increment_odometer(self, kilometers):
        """Incrementa los kilometros en el odometro"""
        self.odometer_reading += kilometers

#primera instancia definida
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
#se actualiza el atributo directamente desde la instancia
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#se actualiza el atributo a tráves de un método
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#segunda instancia definida
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

#se incrementa el atributo a tráves de un método
my_used_car.increment_odometer(100)
my_used_car.read_odometer()