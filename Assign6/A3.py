def printDict(start, end):
    resDict = {x : x**2 for x in range(start, end+1)}
    print(f"Result: {resDict}")

printDict(1,20)