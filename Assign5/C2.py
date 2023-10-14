dict1 = {'key1': 1, 'key2': 3, 'key3': 2} 
dict2 = {'key1': 1, 'key2': 2}

for ele in dict1:
    if ele in dict2 and dict1[ele] == dict2[ele]:
        print(f"{ele} : {dict1[ele]} is present in both x and y")
