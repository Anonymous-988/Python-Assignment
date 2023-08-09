num = int(input("Enter a number: "))

for i in range(2, num+1):
    if i == 2:
        print(i,end=" ")
    else:
        flag = 0
        for j in range(2, i//2 + 1):
            if(i%j == 0):
                flag = 1
                break
        if not flag:
            print(i, end=" ")
else:
    print("Not prime numbers in this range")