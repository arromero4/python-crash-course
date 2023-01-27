favoriteNumber = {
    'Melissa': [26, 7, 22],
    'Gian': [22,4,26],
    'Karen': [9,12,14],
    'Beatriz': [16,4,52],
    'Leticia': [28,52]
    }

for name, favorite in favoriteNumber.items():
    print(f"{name} favorite number:")
    for numbers in favorite:
        print(numbers)