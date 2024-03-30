print('--------------function to calculate the area of a rectangle --------------')


def rectangle_area(l, w):
    a = l * w
    return a


Length = float(input('Please Enter Length of Rectangle: '))
Width = float(input('Please Enter Width of Rectangle: '))

Area = rectangle_area(Length, Width)
print('Area of Rectangle= ', Area)
