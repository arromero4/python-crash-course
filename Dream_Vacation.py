places = {}

#flag to stop the while loop
poll_active = True

while poll_active:
    #asking questions to the user
    name = input("\n What's your name? ")
    response = input("\nIf you could visit one place in the world, where would you go? ")

    #store the answer in the dictionary
    places[name] = response

    #find out if anyone else is going to take the poll
    repeat = input("\nEnter 'yes or no' when you are finished.")
    if repeat == 'no':
        poll_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in places.items():
    print(f"{name} wants to go to {response} one day!")