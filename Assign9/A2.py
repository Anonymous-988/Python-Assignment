class StringOperations:
    def __init__(self):
        self.str = ''

    def getString(self):
        self.str = input("Enter a String: ")

    def printString(self):
        print(f"Entered string is {self.str.upper()}")

    def reverseStr(self):
        revStr = self.str[::-1].lower()
        print(f"Reversed {self.str} is {revStr}")

strObj = StringOperations()
strObj.getString()
strObj.printString()
strObj.reverseStr()
