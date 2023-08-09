tuple1 = (1, 2, 3, 5, 6 , 7, 5, 7)
dupList = []
len = len(tuple1)
for i in range(len):
    for j in range(1, len):
        if tuple1[i] == tuple1[j]:
            dupList.append(tuple1[i])
            break

if len(dupList):
    print(f"Duplicate values are: {dupList}")
else:
    print("No duplicates found")