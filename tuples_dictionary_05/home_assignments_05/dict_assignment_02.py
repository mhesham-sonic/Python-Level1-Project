print('---------------------Join multi tuples into 1 dictionary ----------------------')

person_1_tuples = (101, 'Ahmed Essam', 5000.0, 'Cairo', '0127454104')
person_2_tuples = (102, 'Mohamed Omar', 6000.0, 'Alex', '01147041564')
person_3_tuples = (103, 'Amr Hesham', 7000.0, 'Port Said', '01032659878')
total_tuples_list = [person_1_tuples ,person_2_tuples ,person_3_tuples]
total_persons_list = ['person_1', 'person_2','person_3']
dict_person = {}

for i in range(len(total_persons_list)):
    dict_person[total_persons_list[i]] = total_tuples_list[i]

print(dict_person)