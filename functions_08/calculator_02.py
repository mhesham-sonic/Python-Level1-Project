import sys

print('-------------------------Calculator Function-------------------------')


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        print('Invalid Operation')
        sys.exit()  # it exists the function and doesn't respond to calling 


sum1 = add(2, 3)
diff1 = subtract(5, 9)
product = multiply(25, 10)
print(sum1, diff1, product)

quotionet = divide(70, 5)
print(quotionet)
