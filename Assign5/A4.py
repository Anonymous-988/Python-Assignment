dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

keySearch = int(input("Enter key to Search: "))

if keySearch in dict1:
    print(f"Key found")
else:
    print(f"Key not found")