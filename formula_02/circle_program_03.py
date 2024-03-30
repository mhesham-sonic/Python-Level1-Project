import math

print('---------------calculating perimeter and area of circle---------------')

radius = 7
perimeter = 2 * math.pi * radius
area = math.pi * math.pow(radius,2)

perimeter = round(perimeter,2)
area = round(area,2)


print('Perimeter of Circle= ' + str(perimeter))
print('Area of Circle= ' + str(area))
