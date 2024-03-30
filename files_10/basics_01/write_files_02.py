print('-------------------How to write on files----------------')

print('-------------------Method-1----------------')
file4 = open("C:\\my_files\\write_data.txt", 'w')
file4.write('Let us learn python\n')
file4.write('Python is better than c++\n\n')
file4.write('oracale database linked with python\n')
file4.close()

print('-------------------Method-2----------------')
with open("C:\\my_files\\write_data.txt", 'a') as file5: # w: will overwrite and a: will append
    file5.write('----------------------\n')
    file5.write('I love CCNA and Nokia\n')
    file5.write('Network Engineer and Software Engineer\n\n')
    file5.write('Ramadan Kareem , I want to live outside Egypt')

