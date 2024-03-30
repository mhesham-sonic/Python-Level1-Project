print('-----------Program to Print out Student grade based on conditional IF-----------')

grade = str(input('Please Enter Student Grade : '))

if grade == 'A':
    print('Student Rank: Excellent')
elif grade == 'B':
    print('Student Rank: Very Good')
elif grade == 'C':
    print('Student Rank: Good')
elif grade == 'D':
    print('Student Rank: Pass')
elif grade == 'E':
    print('Student Rank: Fail')
else:
    print('Invalid Input : Please Try Again')
