set1 = set([1,2,3,4,5])

length = 0
for i in set1:
    length += 1

print(f"Set 1 is: {set1}")
print(f"Using Brute Force, Length of the set is {length}")
print(f"Using len(), Length of the set is {len(set1)}")
