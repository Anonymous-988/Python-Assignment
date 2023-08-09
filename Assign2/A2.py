str = input("Enter a string: ")
if len(str)<2:
    print("Empty string")
else:
    new = str[:2]+str[-2:]
    print(f"New String: {new}")