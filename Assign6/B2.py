def calculateGCD(a, b):
    if b == 0:
        return a
    else:
        return calculateGCD(b, a % b)

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the GCD using the recursive function
res = calculateGCD(num1, num2)

# Display the GCD
print(f"The GCD of {num1} and {num2} is: {res}")