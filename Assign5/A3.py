dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}

newDict = {**dict1, **dict2, **dict3}

print(f"Dictionary 1 is: {dict1}")
print(f"Dictionary 2 is: {dict2}")
print(f"Dictionary 3 is: {dict3}")

print(f"Updated Dictionary: {newDict}")