import sys

print('--------------Division by zero----------------')


def math_div(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print('Division by zero is not allowed!')
    if b == 0:
        sys.exit()
    else:
        return result


print('Division Output = ', math_div(15, 0))
