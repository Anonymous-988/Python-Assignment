import re

numLists = []

with open("C1.txt", 'r') as file:
    numList = re.findall(r'\b\d+\b', file.read())

oddList = []
evenList = []

for num in numList:
    num = int(num)
    if(num % 2 == 0):
        evenList.append(num)
    else:
        oddList.append(num)

with open("C1Even.txt", 'w') as evenFile, open("C1Odd.txt", 'w') as oddFile:
    for num in oddList:
        oddFile.write(str(num) + "\n")

    for num in evenList:
        evenFile.write(str(num) + "\n")
