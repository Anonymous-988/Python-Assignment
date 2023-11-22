"""
Define a class Date(Day, Month, Year) with functions to accept and display it. Accept date
from user. Throw user defined exception “invalidDateException” if the date is invalid.
"""

class DateClass:
    def __init__(self, day=1, month=1, year=1000) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"
    
# Initialized variables
inputDay, inputMonth, inputYear = 1, 1, 1000
dateObj = ""
try:
    inputDay = int(input("Enter Day: "))
    inputMonth = int(input("Enter Month: "))
    inputYear = int(input("Enter Year: "))

    if inputYear<1000 or inputYear>9999: #Check for invalid Year
        raise Exception("Invalid Year")
    elif inputMonth<1 or inputMonth>12: #Check for invalid Month
        raise Exception("Invalid Month")
    elif inputMonth in [1,3,5,7,8,10,12] and (inputDay<1 or inputDay>31): #Check for Valid months with 31 days
        raise Exception("Invalid Date")
    elif inputMonth in [4,6,9,11] and (inputDay<1 or inputDay>30):  #Check for Valid months with 30 days
        raise Exception("Invalid Date")
    elif inputYear%4!=0 and inputMonth==2 and (inputDay<1 or inputDay>28): #Check for Valid dates in Feb other than leap year
        raise Exception("Invalid Date")
    elif inputMonth==2 and (inputDay<1 or inputDay>29):  #Check for Valid dates in Feb on a leap year 
        raise Exception("Invalid Date")
    else:
        dateObj = DateClass(inputDay, inputMonth, inputYear)

except Exception as e:
    print(f"Error: {e}")

finally:
    print(f"Input Date was: {dateObj}")