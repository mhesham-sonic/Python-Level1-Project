print('----------------Get sum of even & odd---------------')


def get_sum_even(list1):
    total_even = 0
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            total_even = total_even + list1[i]
    return total_even


def get_sum_odd(list1):
    total_odd = 0
    for i in range(len(list1)):
        if list1[i] % 2 != 0:
            total_odd = total_odd + list1[i]

    return total_odd


x = get_sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Sum of Even Numbers in List= ', x)

y = get_sum_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Sum of Odd Numbers in List= ', y)
