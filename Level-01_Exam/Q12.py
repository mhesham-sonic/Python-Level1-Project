print('----------------Print Reverse string--------------')


def string_reverse(str1):
    list1 = str1.split()
    list1.reverse()
    str2 = ' '.join(list1)
    return str2


input_string = "i like this program very much"
print(string_reverse(input_string))
