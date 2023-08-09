str = input("Enter a string: ")
freqMap = {}

for i in str:
    if i not in freqMap.keys():
        freqMap[i] = 1
    else:
        freqMap[i] += 1

print(freqMap)