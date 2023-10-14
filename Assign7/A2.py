lineCounter = 0

fileName = input("Enter filename: ")

with open(fileName,'r') as file:
    for line in file:
        lineCounter += 1

print(f"Total Number of lines in {fileName} are {lineCounter}")