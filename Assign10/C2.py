"""
Write a function called safe (func, *args) that runs any function using apply, catches any
exception raised while the function runs, and prints the exception using the exc_type and
exc_value attributes in the sys module. Then, use your safe function to run the oops
function you wrote in Exercises 3. Put safe in a module file called tools.py, and pass it the
oops function interactively. Finally, expand safe to also print a Python stack trace when an
error occurs by calling the built-in print_exc() function in the standard traceback module
(see the Python library reference manual or other Python books for details)
"""

from tools import safe

# Opps() function to test with the safe function
def oops():
    raise IndexError("Index out of Bounds")

if __name__ == "__main__":
    safe(oops)
