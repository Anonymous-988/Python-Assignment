inputFile = input("Enter filename: ")
inputLine = int(input("Enter wanted num of lines: "))

lines = []

with open(inputFile, 'r') as file:
    lines = file.readlines()

if inputLine > len(lines):
    print(f"Input num of lines cannot exceed {len(lines)}")
    exit()

reqLines = lines[-inputLine:]
# print(reqLines)
for line in reqLines:
    print(line, end="")
    