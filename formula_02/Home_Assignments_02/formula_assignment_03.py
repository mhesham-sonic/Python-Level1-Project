import math

print('------------------program to calculate volume and area of sphere--------------')

r = int(input('Please select radius value = '))

V = 4/3 * math.pi * math.pow(r,3)
A = 4 * math.pi * math.pow(r, 2)

print('V = ', V)
print('A = ', A)
V = round(V, 2)
A = round(A, 2)
print('V = ', V)
print('A = ', A)
