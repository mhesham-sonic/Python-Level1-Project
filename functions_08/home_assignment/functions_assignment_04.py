print('-------------------Returning sum and number of pos and neg numbers in list-------------')


def pos_neg_list(list1):
    count_pos = 0
    count_neg = 0
    sum_pos = 0
    sum_neg = 0
    for i in range(len(list1)):
        if list1[i] >= 0:
            count_pos = count_pos + 1
            sum_pos = sum_pos + list1[i]
        elif list1[i] < 0:
            count_neg = count_neg + 1
            sum_neg = sum_neg + list1[i]
    print('Number of Positive elements in list = ', count_pos)
    print('Sum of Positive elements in list = ', sum_pos)
    print('Number of Negative elements in list = ', count_neg)
    print('Sum of Negative elements in list = ', sum_neg)


list_num = [1,2,-3,-4,-5,7,8,-9,-10]
pos_neg_list(list_num)
