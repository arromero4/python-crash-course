#making_pizza_1.py

def make_pizza(size, *toppings):
    """Muestra las pizzas que se harán
        Ejemplo tomado de Python Crash Course
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")