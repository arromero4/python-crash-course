pizzas = ['pepperoni','Hawaiian ', 'Cheese', 'Mexican']
friend_pizzas = pizzas[:]
pizzas.append('Mushrooms')
friend_pizzas.append('Bacon') 

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("---------------------")
print("My friend’s favorite pizzas are:")
for friendpizza in friend_pizzas:
    print(friendpizza)
