def findUnion(str1, str2):
    set1, set2 = set(str1), set(str2)
    return set1.union(set2)

def findIntersection(str1, str2):
    set1, set2 = set(str1), set(str2)
    return set1.intersection(set2)

inputStr1 = input("Enter first string: ")
inputStr2 = input("Enter second string: ")

resUnion = findUnion(inputStr1, inputStr2)
resIntersection = findIntersection(inputStr1, inputStr2)

print(f"Union between two strings is: {''.join(resUnion)}")
print(f"Intersection between two strings is: {''.join(resIntersection)}")