import math

print('-----------program to solve math Quadratic equation------------')

a = int(input('Please Select a value = '))
b = int(input('Please Select b value = '))
c = int(input('Please Select c value = '))

part_01 = math.pow(b,2) - (4 * a * c)
part_02 = math.sqrt(part_01)
result = (-b + part_02) / (2 * a)

print('Result = ',result)
result = round(result, 2)
print('Result = ',result)