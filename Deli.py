sandwich_orders = ['pastrami','meatball', 'chicken', 'beef steak','pastrami','cheese','pastrami']
finished_sandwiches = []

print("The Deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    ate_sandwich = sandwich_orders.pop()
    print(f"I made your {ate_sandwich} sandwich")
    finished_sandwiches.append(ate_sandwich)
print(finished_sandwiches)
