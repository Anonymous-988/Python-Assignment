"""
Change the oops function you just wrote to raise an exception you define yourself, called
MyError, and pass an extra data item along with the exception. Then, extend the try
statement in the catcher function to catch this exception and its data in addition to
IndexError, and print the extra data item.
"""

class MyError(Exception):
    def __init__(self, message, data) -> None:
        super().__init__(message)
        self.data = data

def oops(data):
    raise MyError(f"Custom Error Caught ", data)
    raise IndexError("Index out of Bounds")

try:
    data = input("Enter your Data: ")
    oops(data)
except Exception as err:
    print(f"{err.__class__.__name__}: {err} with data => {err.data}")