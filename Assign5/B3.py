from collections import Counter

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}

combinedDict = {}

# Logical Way

# for ele in dict1:
#     if ele in dict1 and ele in dict2:
#         combinedDict[ele] = dict1[ele] + dict2[ele]
#         continue
#     combinedDict[ele] = dict1[ele]

# for ele in dict2:
#     if ele not in combinedDict:
#         combinedDict[ele] = dict2[ele]


# Using Counter from Collections modules
combinedDict = Counter(dict1) + Counter(dict2)

print(f"New Dictionary: {combinedDict}")