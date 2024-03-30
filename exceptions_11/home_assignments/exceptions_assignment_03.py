print('-----------------Reading non Integer Value-------------')
try:
    x = int(input('Please Input Integer No.:'))
    print('This Number is Integer')
except ValueError:
    print('This Number is Not Integer')
