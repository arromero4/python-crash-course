class Dog:

    """Un ejemplo con un perrito"""
    #metodos de la clase
    def __init__(self, name, age):
        """Se inician el nombre y la edad del perriro"""
        self.name = name
        self.age = age
    def sit(self):
        """Simula el comando para que el perrito se siente"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simula una orden para que el perrito gire"""
        print(f"{self.name} rolled over!")
    
my_dog = Dog('Willie', 6)
print(f"Mi perrito se llama: {my_dog.name}.")
print(f"La edad de mi perrito es: {my_dog.age}.")

my_dog.sit()
my_dog.roll_over()