file_path = '/home/arromero/Documents/python3/python-crash-course/text_files/learning_python.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    if "Python" in line:
        print(line.replace("Python","C"))


