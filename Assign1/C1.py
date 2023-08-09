numlist = [1,2,3,4,5,6,7,8]
key = int(input("Enter num to search: "))
left = 0
right = len(numlist)-1
while left <= right:
    mid = (left + right) // 2
    if numlist[mid] == key:
        print(f"Key found at {mid}")
        break
    elif numlist[mid] < key:
        left = mid+1
        continue
    else:
        right = mid-1
        continue
else:
    print("Element not found in the list")

# Solution 2
def BSearch(left, right, numList, key) -> int:
    if left<=right:
        mid = (left + right) // 2
        if numList[mid] == key:
            # print(f"Element found at {mid}")
            return mid
        elif numList[mid] < key:
            return BSearch(mid+1 , right, numList, key)
        else:
            return BSearch(left, mid-1, numList, key)
    else:
        print("Element not found")
        return -1

# print(f"Index of the {key} is: {BSearch(0,len(numlist)-1, numlist, key)}")