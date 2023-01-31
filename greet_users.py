def greet_users(names):
    """
     Muestra un simple saludo para cada usuario en la lista
    ejemplo tomado del libro Python Crash Course   
    """
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['Melissa', 'Andres', 'Arturo']
greet_users(usernames)