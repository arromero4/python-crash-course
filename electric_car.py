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

class Battery:
    """Una clase que muestra la bateria para un auto electrico
    """
    def __init__(self, battery_size=75):
        """Inicia los atributos de una batería"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Muestra una descripción del tamaño de la bateria del auto."""
        print(f"Este auto tiene una bateria de {self.battery_size}-kWh.")

    def get_range(self):
        """Muestra el rango de kilometros que la bateria proporciona."""
        
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"Este auto puede ir cerca de {range} kilometros con carga completa.")

    def upgrade_battery(self):
        """check the battery size and set capacity to 100"""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh")
        else:
            print("The battery is already upgraded")


class ElectricCar(Car):
    """Representa aspectos de un auto, especificamente de autos electricos.
        Inicia atributos especificos para un auto electrico.
    """

    def __init__(self, make, model, year):
        """Inicia los atributos de la clase padre"""
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """Un auto electrico no necesita gasolina"""
        print("Este auto no necesita un tanque de gasolina!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()