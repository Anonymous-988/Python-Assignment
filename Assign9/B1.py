import math

class Circle:
    def __init__(self, radius, center = []) -> None:
        self.radius = radius
        self.center = center

    def printCircle(self):
        print(f"Center Coordinates are: {self.center}")
        print(f"Radius is of {self.radius} units")

    def calculateArea(self):
        return round(math.pi * self.radius ** 2, 2)
    
inputRadius = int(input("Enter radius: "))
inputCenterCoord = [int(input("Enter x Coord: ")), int(input("Enter y Coord: "))]
circleObj = Circle(inputRadius, inputCenterCoord)
circleObj.printCircle()
print(f"Area of the Circle is {circleObj.calculateArea()} sq. units")
