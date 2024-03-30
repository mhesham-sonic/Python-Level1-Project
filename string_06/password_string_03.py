print('--------------password validation-----------')
pwd_str = 'sr@m@_F0rtu9e$._2023'
count_lower, count_upper, count_special, count_digits, total_characters = 0, 0, 0, 0, 0

for i in range(len(pwd_str)):
    if pwd_str[i].islower():
        count_lower = count_lower + 1
    elif pwd_str[i].isupper():
        count_upper = count_upper + 1
    elif pwd_str[i].isdigit():
        count_digits = count_digits + 1
    elif not pwd_str[i].isalnum():
        count_special = count_special + 1

total_characters = count_lower + count_upper + count_special + count_digits

if total_characters >= 8:
    if count_lower >= 1 and count_upper >= 1 and count_special >= 1 and count_digits >= 1:
        print('Strong Password : Accepted')
    else:
        print('Weak Password : Rejected')
else:
    print('Invalid Password')

print(count_lower, count_upper, count_special, count_digits, total_characters)
