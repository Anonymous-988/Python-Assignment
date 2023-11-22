class Calculator:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return (self.num1 + self.num2)
    
    def sub(self):
        return (self.num1 - self.num2)
    
    def multiply(self):
        return (self.num1 * self.num2)
    
    def divide(self):
        if self.num2 == 0:
            print("Undefined (Cannot divide by Zero)")
            return None
        return (self.num1 / self.num2)
    
    def modulus(self):
        return (self.num1 % self.num2)
    
inputNum1 = int(input("Enter a Number 1: "))
inputNum2 = int(input("Enter a Number 2: "))

CalculatorObj = Calculator(inputNum1, inputNum2)
operations = [CalculatorObj.sum(), CalculatorObj.sub(), CalculatorObj.multiply() , CalculatorObj.divide(), CalculatorObj.modulus()]

print("1. Add")
print("2. Subtract")
print("3. Multiple")
print("4. Divide")
print("5. Modulus")
choice = int(input("Choose one of the options: "))
result = operations[choice-1]

print(f"Result +> {result}")