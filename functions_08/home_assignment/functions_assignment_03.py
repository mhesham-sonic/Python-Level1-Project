print('-------------------program to check prime numbers--------------------')


def isprime(a):
    check = True
    if a > 0:
        for i in range(2, 10):
            if a % i == 0 and i != a:
                check = False
                break
    else:
        print('Invalid Input')

    if check and a >= 2:
        print('This Number is Prime')
    elif not check and a != 0 or a == 1:
        print('This Number is not Prime')


x = int(input('Please check if this Number is Prime or Not: '))
isprime(x)

