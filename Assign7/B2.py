import re

inputFile = input("Enter filename to search: ")
inputKey = input("Enter a word to search: ")

keyCounter = 0

with open(inputFile, 'r') as file:
    data = file.read()
    words = re.findall(r'\b\w+\b', data)
    # print(words)
    keyCounter = words.count(inputKey)
    # print(keyCounter)

print(f"{inputKey} occurs {keyCounter} times in {inputFile}")


