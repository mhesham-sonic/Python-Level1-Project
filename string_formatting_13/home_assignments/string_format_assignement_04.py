print('-------------------Phone Number------------')


def format_phone_number(number):
    x = number[0]
    y = number[1:4]
    z = number[4:7]
    w = number[7:]
    return print(f'Phone Number: +{x} ({y}) {z}-{w}')


Num = input('Please Input Phone Number:')
format_phone_number(Num)
