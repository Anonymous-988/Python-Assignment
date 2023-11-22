"""
Should be implemented as module for C2.py program
"""

import traceback

def safe(func, *args):
    try:
        result = func(*args)
        return result
    except Exception as err:
        print(f"{err.__class__.__name__} Caught: {err}")
        traceback.print_exc()