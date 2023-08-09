num = int(input("Enter a number: "))

for i in range(num+1):
    for j in range(num - i):
        print(j+1, end="\t")
    print()