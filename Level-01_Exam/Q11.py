print('------------------Password Validation--------------')


def password_validation(input_string):
    count_upper, count_lower, count_digit, count_special = 0, 0, 0, 0
    for i in range(len(str1)):
        if str1[i].isupper():
            count_upper += 1
        elif str1[i].islower():
            count_lower += 1
        elif str1[i].isdigit():
            count_digit += 1
        elif not str1[i].isalnum():
            count_special += 1

    total = count_upper + count_lower + count_digit + count_special
    print(count_upper, count_lower, count_digit, count_special, total)
    if total >= 8:
        if count_upper >= 1 and count_lower >= 1 and count_digit >= 1 and count_special >= 1:
            check = True
        else:
            check = False
    else:
        check = False

    return check


str1 = 'sr@m@_f0rtu9e$._2023'
print(password_validation(str1))
