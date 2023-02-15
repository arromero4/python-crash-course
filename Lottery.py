from random import choice
players = (1,2,3,4,5,6,7,8,9, 'A','B','C','D','E','F')

chosen = [str(choice(players)) for x in range(4)]
# print the four chosen items
print(f"Any ticket matching {''.join(chosen)} wins a prize!")