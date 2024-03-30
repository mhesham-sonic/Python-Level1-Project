import math

print('-----------How to create functions?-----------')


def numbers_loop(tail):
    sum_numbers = 0
    for i in range(1, tail + 1):
        print(i, end=' ')
        sum_numbers = sum_numbers + i
    print()
    return sum_numbers


# main program
print('-----------Print numbers from 1 to 10 three times-----------')
# function :   name = numbers_loop  |  parameter [ input ] [ argument ]  | return value
# call function [ invoke function ]
total = numbers_loop(10)
print(total)
print('---')
total = numbers_loop(20)
print(total)
print('---')
total = numbers_loop(5)
print(total)
print('---')

result = math.pow(2, 3)
