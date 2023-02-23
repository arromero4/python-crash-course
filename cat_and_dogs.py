def catAndDogs(filename):
    """read the names of the dogs and cats"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        print(contents)

filenames = ['text_files/cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    catAndDogs(filename)