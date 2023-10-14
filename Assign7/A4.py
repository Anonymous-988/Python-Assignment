filename = input("Enter filename: ")

charCounter = 0

with open(filename, 'r') as file:
    for line in file:
        charCounter += len(line)

print(f"{filename} has {charCounter} characters")