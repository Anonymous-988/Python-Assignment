"""
Write text file named test.txt that contains integers, characters and float numbers. Write a
Python program to read the test.txt file. And print appropriate message using exception to
print weather line contains integer, character or float value.
"""

lines = []
try:
    with open("A3.txt", "r") as file:
        lines = file.readlines()
except Exception as err:
    print(f"Error: {err}")

for line in lines:
    try:
        line = eval(line)
        if isinstance(line, int):
            raise Exception(f"{line} is an Interger Value")
        elif isinstance(line, float):
            raise Exception(f"{line} is a Float Value")
            
    except Exception as err:
        if isinstance(err, (NameError,SyntaxError)):
            print(f"Error: {line} is a Character Value")
        else:
            print(f"Error: {err}")