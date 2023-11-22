class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def getMultipliedTime(self, number):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds *= number

        new_hours, remainder = divmod(total_seconds, 3600)
        new_minutes, new_seconds = divmod(remainder, 60)

        return Time(new_hours%12, new_minutes, new_seconds)
    
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


if __name__ == "__main__":
    timeObj = Time(2, 58, 22)
    mulNum = 2

    print(f"Old Time: {timeObj}")
    print(f"New Time: {timeObj.getMultipliedTime(mulNum)}")