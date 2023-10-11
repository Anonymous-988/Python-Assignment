import itertools

dict1 = {'1':['a','b'], '2':['c','d']}

# Get the values (lists of letters) from the dictionary
letterList = dict1.values()

# Use itertools.product to generate all combinations
combinations = itertools.product(*letterList)

# Iterate through the combinations and join the letters
for combination in combinations:
    result = ''.join(combination)
    print(result)
