print('-------------password check----------------------')

current_pwd = '$uper_Man@2025'

i = 0
while i < 3:
    input_pwd = input('Please enter your password: ')
    if input_pwd == current_pwd:
        print('Correct Password : Access Granted')
        break
    i += 1
else:
    print('Wrong Password : Access Blocked for 15 mins')
