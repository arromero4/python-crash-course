rivers = {
    'nilo': 'egypt',
    'amazonian': 'brasil',
    'bravo': 'mexico'
}

for key, values in rivers.items():
    print(f"The {key} runs through {values}")

for key in rivers.keys():
    print(f"The {key} river")

for value in rivers.values():
    print(f"The country {value} of the river")