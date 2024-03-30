print('-------------------checking palindrome---------------')

str1 = '32521'
list1 = []

for i in range(len(str1)):
    list1.append(str1[i])
list1.reverse()
str2 = ''.join(list1)
print(str1)
print(str2)

if str1 == str2:
    print('This String is Palindrome')
else:
    print('This String is Non-Palindrome')

