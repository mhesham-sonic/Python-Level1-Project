print('----- program to handle exceptions -----')
"""
1- happy scenario
2- exception raise and handled
3- exception raise but not handled
"""
try:
    first_number = int(input('please enter 1st number: '))
    second_number = int(input('please enter 2nd number: '))
    result = first_number / second_number
    print('Result =', result)
    open('c:\\my_files\\file1.txt')  # error not handled wrong file path
except ValueError:   # get the type of error from run window below
    print('Invalid Non-Integer Input')
#except ZeroDivisionError:  # get the type of error from run window below
    #print('Error-Division by zero')
except FileNotFoundError:
    print('File does not exist')
finally:
    print('This is the final statement - works anytime')   # this will be executed in the 3 scenarios

print('Continue or End Program ...')
