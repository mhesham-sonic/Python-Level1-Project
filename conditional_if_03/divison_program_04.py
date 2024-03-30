print('-------------------checking if a number is divisible by 2&3&6---------------')

num = int(input('Please Enter the Number= '))

if num % 2 == 0 and num % 3 == 0 and num % 6 == 0:
    print('This Number is Divisible by 2 & 3 & 6')
else:
    print('This Number is Not Divisible by 2 & 3 & 6')
