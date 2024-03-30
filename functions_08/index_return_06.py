print('-----------checking if number exist in list and return its index')


def index_check(list1, a=10):
    """
    :param list1: This is the list to search in
    :param a: this is the int value to search in the list
    :return: return index of param a if found - return -1 if not found
    """
    for i in range(len(list1)):
        if list1[i] == a:
            return i
    return -1


print('ahmwd', 'esam', 'ola', 'omar')  # *args : tuple [ any number of parameters ]
x = index_check([1, 2, 3, 4, 5, 6, 7, 8], 9)  # positional calling (order is mandatory)
y = index_check(a=9, list1=[1, 5, 16, 2])  # named calling (order is not important)
z = index_check(list1=[15, 12, 10])
print(z)
print('test', end='')

print(x)
