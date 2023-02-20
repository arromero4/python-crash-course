
from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities"""
    winning_ticket = []

    """not repeating numbers or letters"""
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        """only add the pulled item to the winning ticket if it hasn't already been pulled"""
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    
    return winning_ticket

def make_random_ticket(possibilities):
    """Return a ticket from a set of possibilities"""
    ticket = []

    """not repeating numbers or letters"""
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        """only add the pulled item to the ticket if it hasn't already been pulled"""
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    
    return ticket

def check_ticket(played_ticket, winning_ticket):
    #Check all elements in the played ticket. if any are not in the winning ticket, return false
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    #we must have a winning ticket
    return True

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket =  get_winning_ticket(possibilities)
plays = 0 #numbers of tries to get a win ticket
won = False #change when we win

max_tries = 1_000_000 #max number of tries, in case this takes forever!

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1

    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")


# chosen = [str(choice(players)) for x in range(4)]
# # print the four chosen items
# print(f"Any ticket matching {''.join(chosen)} wins a prize!")