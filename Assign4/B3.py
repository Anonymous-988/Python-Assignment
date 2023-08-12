set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])

setDiff = set1.difference(set2)

symmetricDiff = set1.symmetric_difference(set2)

print(f"Set 1 is: {set1}")
print(f"Set 2 is: {set2}")
print(f"Set Difference is: {setDiff}")
print(f"Symmetric Difference is: {symmetricDiff}")