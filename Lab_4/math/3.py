import math
sides = int(input("Input number of sides: "))
leng = int(input("Input the length of a side: "))

print(("The area of polygon is:"), math.floor((sides * leng**2) / (4 * math.tan(math.pi/sides))))