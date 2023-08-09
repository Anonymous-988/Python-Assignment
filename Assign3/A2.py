num = int(input("Enter length of tuple: "))
tuple1 = ()
for i in range(num):
    ele = int(input("Enter a number: "))
    tuple1 = tuple1 + (ele,)

print(tuple1)
print(tuple1[3])