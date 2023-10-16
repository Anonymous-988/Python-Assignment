import math

class Shape:
    def __init__(self) -> None:
        pass

    def area(self):
        return 0
    
    def volume(self):
        return 0
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3
    
class Square(Shape):
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2
    
    def volume(self):
        return self.side ** 3
    

inputSide = int(input("Enter side length of Square: "))
squareObj = Square(inputSide)
print(f"Area of the square: {squareObj.area()}")
print(f"Volume of the square: {squareObj.volume()}")

inputRadius = int(input("Enter Radius of Circle: "))
circleObj = Circle(inputRadius)
print(f"Area of the Circle: {circleObj.area()}")
print(f"Volume of the Circle: {circleObj.volume()}")