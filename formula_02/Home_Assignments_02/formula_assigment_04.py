import math

print('-----------program to solve math equation------------')

i = int(input('Please Select i value = '))

part_01 = 1 + i * math.sqrt(2)
part_02 = 2 - 3 * i
part_03 = 3 + i
result = part_01 * part_02 * part_03

print('Result = ' + str(result))
result = round(result, 2)
print('Result = ',result)
