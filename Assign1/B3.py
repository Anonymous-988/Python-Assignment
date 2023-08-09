import math

coord1 = input("Enter coord1(comma separated): ").split(",")
coord2 = input("Enter coord2(comma separated): ").split(",")

x1, y1 = int(coord1[0]), int(coord1[1])
x2, y2 = int(coord2[0]), int(coord2[1])

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
dist = round(dist, 2)
print(f"Distance between two coord is {dist}")