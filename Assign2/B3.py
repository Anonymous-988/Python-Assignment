str = input("Enter a string: ")
freqMap = {}

for i in str:
    if i not in freqMap.keys():
        freqMap[i] = 1
    else:
        freqMap[i] += 1

for ch in freqMap:
    print(f"{ch} count is {freqMap[ch]}")