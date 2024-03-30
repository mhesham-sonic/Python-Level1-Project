print('---------------function to check if no. is even or odd-------------')

"""
def no_check(a):
    if a % 2 == 0:
        return True
    else:
        return False
"""
"""
def no_check(a):
    check_even = False
    if a % 2 == 0:
        check_even = True

    return check_even
"""


def no_check(a):
    return a % 2 == 0


is_even = no_check(4)

if is_even:
    print('This No is Even')
else:
    print('This No is Odd')
