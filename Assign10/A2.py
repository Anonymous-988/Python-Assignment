"""
Define a custom exception class which takes a string message as attribute
"""


class UserDefinedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

inputUsername = ""
try:
    inputUsername = input("Enter Username: ")
    if inputUsername != "Sumant":
        raise UserDefinedException(f"{inputUsername} is an unauthorised user")
    else:
        print("Welcome Sumant!!!")
except UserDefinedException as e:
    print(f"Custom Error: {e}")
