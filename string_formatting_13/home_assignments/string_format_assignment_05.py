import math

print('-------------percentage and decimal value-----------')


def format_percentage(decimal):
    z = decimal.index('.')
    y = decimal[0:z]
    w = decimal[z+1:z+3]
    return print(f'Percentage Value = {y}.{w}%')


x = input('Please Enter the Value: ')
format_percentage(x)
