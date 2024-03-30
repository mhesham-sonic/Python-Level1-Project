print('--------------print word in alphabetical order---------------')
str1 = 'english'
str2 = ''
list1 = []
list2 = []
list3 = []
if str1 != 'python':
    for i in range(len(str1)):
        list1.append(str1[i])
    list1.sort()
    str2 = ''.join(list1)
    print(str2)
else:
    for j in range(len(str1)):
        list2.append(str1[j])
    for z in range(1, len(list2)):
        list3.append(list2[z])
        list3.sort()
    str3 = ''.join(list3)
    print('P' + str3)



