print('-------------------function to get min and max of list-----------------')


def min_max_list(list1):
    min_item = list1[0]
    max_item = list1[0]
    for i in range(len(list1)):
            if list1[i] > max_item:
                max_item = list1[i]
            elif list1[i] < min_item:
                min_item = list1[i]
    print('Max Number in list = ', max_item)
    print('Min Number in list = ', min_item)


list_num = [77, 49, 53, 61, 80, 100]
min_max_list(list_num)



