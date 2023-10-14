inputStr = input("Enter a String: ")

def recursiveReverse(str):
    if len(str) == 0:
        return
    print(str[-1], end="")
    recursiveReverse(str[:-1])

recursiveReverse(inputStr)