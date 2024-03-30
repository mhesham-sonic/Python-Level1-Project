import math

print('-----------program to solve math equation------------')

i = int(input('Please Select i value = '))

part_01 = math.pow((1 + i),3)
part_02 = math.pow((1-i),5)

result = part_01 / part_02
print('Result = ',result)

