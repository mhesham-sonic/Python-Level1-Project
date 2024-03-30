print('-----Program to calculate operation on 2 numbers Bonus based on conditional IF--------')

first_input = float(input('Please Enter 1st Number: '))
operation = str(input('oper: '))
second_input = float(input('Please Enter 2nd Number: '))

if operation == '+':
    result = first_input + second_input
    print('Result: ' + str(first_input) + str(operation) + str(second_input) + '=' + str(result))
elif operation == '-':
    result = first_input - second_input
    print('Result: ' + str(first_input) + str(operation) + str(second_input) + '=' + str(result))
elif operation == '*':
    result = first_input * second_input
    print('Result: ' + str(first_input) + str(operation) + str(second_input) + '=' + str(result))
elif operation == '/':
    result = first_input / second_input
    print('Result: ' + str(first_input) + str(operation) + str(second_input) + '=' + str(result))
else:
    print('Invalid Operation : Please Try Again')