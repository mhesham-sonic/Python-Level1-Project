print('-------------Printing last part of IP in case of yes----------')

ips_list = [
('192.168.0.15', 'y'),
('192.168.0.22', 'y'),
('192.168.0.14', 'y'),
('192.168.0.24', 'n'),
('192.168.0.81', 'n'),
('192.168.0.11', 'y')
]

list1 = []
for i in range(len(ips_list)):
    if ips_list[i][1] == 'y':
        list1 = ips_list[i][0].split('.')
        print(list1[-1])