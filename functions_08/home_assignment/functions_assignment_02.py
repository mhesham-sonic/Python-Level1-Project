print('-------------------function to check if a string is a palindrome -----------')


def palindrome_check(str1):
    str1 = str1.lower()
    list1 = []
    for i in range(len(str1)):
        list1.append(str1[i])
    list1.reverse()
    str2 = ''.join(list1)
    print(str1)
    print(str2)
    check = False
    if str1 == str2:
        check = True
        print('This String is Palindrome')
    else:
        print('This String is Non-Palindrome')


text1 = input('Please Enter your String: ')
palindrome_check(text1)

