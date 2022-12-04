current_users = ['Melissa', 'Gian', 'Randy', 'Karen','Beatriz','Leticia','Rafael','Andres','Admin']
current_users_copy = [x.lower() for x in current_users]

new_user = ['Diego','Lupita','Abelardo', 'Andres',]

for user in new_user:
    if user.lower() in current_users_copy:
        print(f"Sorry {user}, that name is taken. You will need to enter a new username")
    else:
        print(f"Username: {user} is available.")