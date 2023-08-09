num = int(input("Enter a number: "))

# Solution 1

fibList = [0,1]

if num == 1 or num==2:
    print(fibList[:num])
    exit()

for i in range(1, num-1):
    fibList.append(fibList[i]+fibList[i-1])

print(fibList)

# Solution 2

def FibList(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return (FibList(num-1)+FibList(num-2))
    

for i in range(1,num+1):
    print(FibList(i), end=" ")

