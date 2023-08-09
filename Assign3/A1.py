num = int(input("Enter a number: "))

list = []

for i in range(1, num+1):
    list.append((i, i**2))

print(list)