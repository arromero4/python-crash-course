message = "\nPlease enter the topping you want in your pizza: "
message += "\nEnter 'quit' when you are finished."


#form 1
while True:
    topping = input(message)
    if topping == 'quit':
        break
    else:
        print(f"you’ll add {topping} to your pizza.")

#form 2
# active = True
# while active:
#     topping = input(message)
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"you’ll add {topping} to your pizza.")