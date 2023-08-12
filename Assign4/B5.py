set1 = set([1,2,3,4,5])

minimum = 99999999
maximum = 0

for i in set1:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i

print(f"Set 1 is: {set1}")
print(f"Using Brute Force, Max is {maximum} and Min is {minimum}")
print(f"Using Min() and Max(), Max is {max(set1)} and Min is {min(set1)}")