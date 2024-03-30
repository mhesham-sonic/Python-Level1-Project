# show strings functions
print('---- Create and print string ----')
emp_name = 'Mohamed Hesham'
print(emp_name)
print(type(emp_name))

print('-------- upper(), lower() functions -------------')
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(emp_name)
print(upper_emp_name)
print(lower_emp_name)

print('------ isupper(), islower(), isalpha() functions --- True , False --')
print(upper_emp_name.isupper())
print(lower_emp_name.islower())
print(lower_emp_name.isupper())
emp_id = '101'
print(emp_id.isdigit())
print(emp_id.isalpha())
print(emp_id.isalnum())
emp_id = '10 1'
print(emp_id.isdigit())
print(emp_id.isalpha())
print(emp_id.isalnum())

print('-------------- endsWith() function -----------------')
file_path = 'C:\\root\\documents\\courses\\CCNA.PDf'
file_path = file_path.lower()  # ignore case
if file_path.endswith('pdf'):
    print('File Type : Book')
elif file_path.endswith('xlsx') or file_path.endswith('xls'):
    print('File Type : Excel sheet')
else:
    print('Unknown Type')

print('-------------- startswith() function ---------')
emp_mobile = '+201275244763'
print(emp_mobile)
if emp_mobile.startswith('+20'):
    print('Employee Country : Egypt')
elif emp_mobile.startswith('+266'):
    print('Employee Country : Saudi Arabia')
else:
    print('Unknown Country Code')

print('------ in membership --------------')
emp_cv = 'Iam a programmer, iam interested in python, java'
emp_cv = emp_cv.lower()
if 'python' in emp_cv and 'java' in emp_cv:
    print('Highly Recommended')
if 'python' in emp_cv:
    print('Suitable')
else:
    print('Not Suitable for Job')

print('-------------- count function -----------')
emp_cv = 'Iam a programmer, iam interested in python, java, python , php , python, Python'
emp_cv = emp_cv.lower()
python_count = emp_cv.count('python')
print(python_count)

print('---------- index(),  replace() functions |  slicing ---------------')
emp_email = 'Mohamed.Aly@gmail.com'
print(emp_email.index('@'))
user_name = emp_email[0: emp_email.index('@')]
domain = emp_email[emp_email.index('@') + 1:]  # : without end means till the end
print(user_name)
print(domain)
emp_email = emp_email.replace('.', '_', 1)
print(emp_email)

print('--------------- Looping :  Loop over letters of string using index for i -----------------------')
print(emp_email)
for i in range(len(emp_email)):
    print(emp_email[i])

print('--------------- Looping :  Loop over letters of string using for each item -----------------------')
print(emp_email)
for item in emp_email:
    print(item)

print('-------- split() function ------ to split string into list of words ---------------')
ip = '172.16.0.1'
octet_list = ip.split('.')  # if ip.split() without input : it will separate by space
print(octet_list)
print(octet_list[1])
octet_list[2] = '11'
print(octet_list)

print('------ return the list back to string using join() function --------')
new_ip = '.'.join(octet_list)
print(new_ip)

print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')
