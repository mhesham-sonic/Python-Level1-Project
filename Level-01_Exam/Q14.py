print('----------Remove all characters except letters and numbers---------')


def non_alphanum_removal(str1):
    list1 = []
    for i in range(len(str1)):
        if str1[i].isalnum():
            list1.append(str1[i])
    str2 = ''.join(list1)
    return str2


ini_string = "123abcjw:, .@! eiw"
print(non_alphanum_removal(ini_string))

