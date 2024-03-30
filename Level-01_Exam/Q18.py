print('------------------Swap 2 numbers without temp---------')


def element_swap(list1, a, b):
    x = str(a)
    y = str(b)
    list2 = []
    list3 = []
    list4 = []

    for item in list1:
        list2.append(str(item))

    str1 = ''.join(list2)
    str1 = str1.replace(x, '$')
    str1 = str1.replace(y, x)
    str1 = str1.replace('$', y)

    for i in range(len(str1)):
        list3.append(str1[i])

    for val in list3:
        list4.append(int(val))

    return list4


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_01 = 3
element_02 = 8
print(element_swap(input_list,element_01,element_02))
print(element_01, element_02)


# element_02, element_01 = (element_01, element_02)
element_01 = element_01 + element_02

