list  = [1,2,3,2,5]
flag = 0
len = len(list)
for i in range(len):
    for j in range(i+1, len):
        if list[i] == list[j]:
            flag = 1
            print(f"Duplicate Found: {list[i]}")
            break

if not flag:
    print("All Values are unique")