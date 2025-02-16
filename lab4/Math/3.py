import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * math.pow(s, 2)) / (4 * math.tan(math.pi / n))
area = round(area, 2)

print("The area of the polygon is:", area)
