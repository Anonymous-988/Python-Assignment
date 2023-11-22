import math

class CircleClass:
    def __init__(self, circleCenterCoords, radius) -> None:
        self.centerXCoord = circleCenterCoords[0]
        self.centerYCoord = circleCenterCoords[1]
        self.radius = radius

    def isPointWithinCircle(self, pointCoords):
        pointXCoord = pointCoords[0]
        pointYCoord = pointCoords[1]

        distance = math.sqrt((pointXCoord - self.centerXCoord)**2 + (pointYCoord - self.centerYCoord)**2)

        return distance <= self.radius
    
if __name__ == "__main__":
    circleCenterCoords = (0, 0)
    circleRadius = 5
    circleObj = CircleClass(circleCenterCoords, circleRadius)

    pointCoords = (5,0)

    if circleObj.isPointWithinCircle(pointCoords):
        print("Point is within the Circle")
    else:
        print("Point is not within the Circle")