set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])

fullJoin = set1 | set2
print(f"Set 1 is: {set1}")
print(f"Set 2 is: {set2}")
print(f"Intersection using pipe operator: {fullJoin}")

fullJoin = set1.union(set2)
print(f"Intersection using Union(): {fullJoin}")