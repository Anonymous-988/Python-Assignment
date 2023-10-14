inputFile = input("Enter source filename: ")
outputFile = input("Enter destination filename: ")

with open(inputFile,'r') as source, open(outputFile, 'w') as destination:
    for line in source:
        destination.write(line.upper())

print(f"Message has been updated to {outputFile}")

print(f"\n\nContents of {outputFile} are: ")
with open(outputFile, 'r') as file:
    for line in file:
        print(line, end="")