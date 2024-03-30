import random

print('----------------Program to verify sum of 2 numbers------------------')

correct_answers = 0
wrong_answers = 0
for i in range(5):      # for (int i = 0; i < 6; i++)   java
    print('---- Question no. ', (i + 1))
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    print(first_number,' + ',second_number,' = ')
    result = int(input(''))

    if result == first_number + second_number:
        print('Correct Answer')
        correct_answers = correct_answers + 1
    else:
        print('Wrong Answer')
        wrong_answers = wrong_answers + 1

print('Correct Answers : ',correct_answers)
print('Wrong Answers : ',wrong_answers)
print('End of the program')


