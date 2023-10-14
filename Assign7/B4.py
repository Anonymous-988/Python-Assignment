inputFile = input("Enter filename: ")

lines = []

with open(inputFile, 'r') as file:
    lines = file.readlines()

reqLines = lines[::-1]
# print(reqLines)
for line in reqLines:
    print(line, end="")