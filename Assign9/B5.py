import os

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            return "Indefinite Number"
        return round(self.num1 / self.num2,2)

    def floor(self):
        if self.num2 == 0:
            return "Indefinite Number"
        return round(self.num1 // self.num2,2)

while True:
    inputNum1 = int(input("Enter 1st Num: "))
    inputNum2 = int(input("Enter 2nd Num: "))
    calcObj = Calculator(inputNum1, inputNum2)
    print("Choose one of the options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Floor Division")
    print("6. Exit")
    choice = int(input("Enter a choice: "))
    
    if choice == 1:
        print(f"{inputNum1} + {inputNum2} = {calcObj.add()}")
    elif choice == 2:
        print(f"{inputNum1} - {inputNum2} = {calcObj.sub()}")
    elif choice == 3:
        print(f"{inputNum1} * {inputNum2} = {calcObj.mul()}")
    elif choice == 4:
        print(f"{inputNum1} / {inputNum2} = {calcObj.div()}")
    elif choice == 5:
        print(f"{inputNum1} // {inputNum2} = {calcObj.floor()}")
    elif choice == 6:
        print(f"Exiting Application")
        break
    else:
        print("invalid Input")
