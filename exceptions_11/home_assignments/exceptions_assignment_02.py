print('---------------average of non integer values---------------')


def calculate_average(list_X):
    try:
        sum_elements = 0
        for i in range(len(list_X)):
            sum_elements = sum_elements + list_X[i]
        avg = sum_elements / len(list_X)
        return avg
    except TypeError:
        print('Error: Non-numeric value found in the list!')


list1 = [10, 20, '30z', 40]
print('Average of elements in list= ', calculate_average(list1))
