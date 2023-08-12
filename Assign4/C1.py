set1 = set([1,2,3,4,5])
set2 = set1
print("Before changes")
print(f"Set 1 is: {set1} and id is: {id(set1)}")
print(f"Set 2 is: {set2} and id is: {id(set2)}")

set2.add(6)

print("\nAfter changes Demonstrating Shallow Copy using asignment operator '='")
print(f"Set 1 is: {set1} and id is: {id(set1)}")
print(f"Set 2 is: {set2} and id is: {id(set2)}")

set2 = set1.copy()

set2.add(7)

print("\nAfter changes Demonstrating Deep Copy using Copy()")
print(f"Set 1 is: {set1} and id is: {id(set1)}")
print(f"Set 2 is: {set2} and id is: {id(set2)}")