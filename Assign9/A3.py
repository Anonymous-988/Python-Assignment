class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.breadth = 0

    def rectArea(self):
        area = self.length * self.width
        print(f"Area of Rectangle is {area} sq. units")

    def rectVolume(self):
        self.breadth = int(input("Enter breadth of Rectangle: "))
        volume = self.length * self.width * self.breadth
        print(f"Area of Rectangle is {volume} cu. units")


inputLength = int(input("Enter Length of the Rectangle: "))
inputWidth = int(input("Enter Width of the Rectangle: "))
rectObj = Rectangle(inputLength, inputWidth)
rectObj.rectArea()
rectObj.rectVolume()

