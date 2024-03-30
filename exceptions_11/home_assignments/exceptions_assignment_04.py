import sys
print('-----------------Index out of list Range-----------')


def list_index(list_x, a):
    try:
        z = list_x[a]
    except IndexError:
        print('Index out of range!')
        sys.exit()
    return z


list1 = [3, 4, 5, 6, 7]
index = 7
print('Element at index ', index, '=', list_index(list1, index))
