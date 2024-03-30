print('-----------------No of occurrence of element in list---------------')


def element_loc_list(list1, a):
    list_occ = []
    for i in range(len(list1)):
        if list1[i] == a:
            list_occ.append(i)
    return list_occ


input_list = [1, 3, 4, 5, 3, 6, 7, 3, 10, 15, 12, 3, 20]
check_element = 3
print(check_element, ' is found at indexes ', element_loc_list(input_list,check_element))