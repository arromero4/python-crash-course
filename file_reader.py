# absolute path
file_path = '/home/arromero/Documents/python3/python-crash-course/text_files/pi_digits.txt'

# with open('text_files//pi_digits.txt') as file_object: <--- relative path
with open(file_path) as file_object:  # using absolute path
    contents = file_object.read()
    for line in contents:
        print(line)
print(contents.rstrip())
print("---------------------------------")
# working with each line of the .txt
with open(file_path) as file_object:  # using absolute path)
    for line in file_object:
        print(line.rstrip())
print("---------------------------------")
# Saving in a list
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())    
print("---------------------------------")