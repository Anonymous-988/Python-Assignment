dupMap = {}
str = input("Enter a String: ")
len = len(str)
for i in range(len):
    if str[i] not in dupMap.keys():
        dupMap[str[i]] = 1
    else:
        str = str[:i] + '$' + str[i+1:]
        break

print(f"New String is {str}")