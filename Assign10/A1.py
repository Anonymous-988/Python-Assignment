"""
Write a Python program to input a positive integer. Display correct message for correct
and incorrect input.
"""

inputNum = 0
try:
    inputNum = int(input("Enter a Positive Number: "))
    if inputNum < 1:
        raise Exception(f"{inputNum} is not a Positive Number")
    print(f"{inputNum} is a Positive Number")
except Exception as e:
    print(f"Custom Error: {e}")