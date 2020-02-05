import os

from_file = 'digits.txt'
to_file = 'C:/Users/rasmu/Documents/Python/Uge5/02-2 Working with Files/newDigits.txt'

if __name__ == '__main__':
    with open(from_file) as file_object:
        lines = file_object.readlines()
        
with open(to_file, 'w') as file_object:
    for line in lines:
        if (line[0].isdigit()):
            file_object.write(line)