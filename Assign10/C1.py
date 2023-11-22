"""
Change the oops function in question 4 from SET A to raise an exception you define
yourself, called MyError, and pass an extra data item along with the exception. You may
identify your exception with either a string or a class. Then, extend the try statement in the
catcher function to catch this exception and its data in addition to IndexError, and print the
extra data item. Finally, if you used a string for your exception, go back and change it be a
class instance.
"""

class MyError(Exception):
    def __init__(self, message, data) -> None:
        super().__init__(message)
        self.data = data

def oops(data):
    if data:
        raise MyError(f"Custom Error Caught", data)
    raise IndexError("Index out of Bounds")

try:
    data = input("Enter your Data: ")
    oops(data)
except Exception as err:
    if isinstance(err, MyError):
        print(f"{err.__class__.__name__}: {err} with data => {err.data}")
    else:
        print(f"{err.__class__.__name__}: {err}")