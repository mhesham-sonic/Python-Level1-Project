print('----------------------Name & Age-------------')


def candidate(x, y, z):
    return print(f'Welcome {x} {y} to our club , Please confirm your age is {z} ?')


first_name = input('Please Enter your First Name: ')
last_name = input('Please Enter your Last Name: ')
age = int(input('Please Enter your Age:'))
candidate(first_name,last_name,age)

