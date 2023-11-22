import datetime

class DateTimeOp:
    def __init__(self) -> None:
        self.currentDatetime = datetime.datetime.now()
        self.DaysList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def getCurrentDate(self):
        return self.currentDatetime.strftime('%d/%m/%Y %H:%m:%S')
    
    def getWeekDay(self):
        return self.DaysList[self.currentDatetime.weekday()];

if __name__ == "__main__":
    dateObj = DateTimeOp()
    print(f"Today's Date is: {dateObj.getCurrentDate()}")
    print(f"Today's Day is: {dateObj.getWeekDay()}")