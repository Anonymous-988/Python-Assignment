"""
Write a function called oops that explicitly raises a IndexError exception when called. Then
write another function that calls oops inside a try/except statement to catch the error.
"""

def oops():
    raise IndexError("Index out of Bounds")

try:
    oops()
except Exception as err:
    print(f"{err.__class__.__name__}: {err}")