numRange = int(input("Enter number range(1-n): "))

dict1 = {x: x*x for x in range(1,numRange+1)}

print(f"Dictionary: {dict1}")