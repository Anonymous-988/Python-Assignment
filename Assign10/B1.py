"""
Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These
brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)",
"({[)]" and "{{{" are invalid using exception.
"""

class EspressionValidator:
    def __init__(self):
        self.openingBracketList = '([{' #implemented a string can use a list as well
        self.bracketPairMap = {')': '(', ']': '[', '}': '{'}
    
    def isValidExpression(self, str):
        stack = []
        for char in str:
            if char in self.openingBracketList:
                stack.append(char)
            elif char in self.bracketPairMap:
                if not stack or stack[-1] != self.bracketPairMap[char]:
                    return False
                stack.pop()
        return not stack
    

try:
    validatorObj = EspressionValidator()
    inputExpression = input("Enter an expression: ")
    if validatorObj.isValidExpression(inputExpression):
        print("This is a valid expression")
    else:
        raise Exception("This is an Invalid Expression")
except Exception as err :
    print(f"Error: {err}")
finally:
    print("Validation complete!!")