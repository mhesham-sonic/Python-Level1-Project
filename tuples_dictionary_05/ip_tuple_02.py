
print('-------------------------')
ips_List = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.11', 'y')
]

print(ips_List)
print(type(ips_List))
print(ips_List[2])
print(ips_List[2][1])

for item in ips_List:
    if item[1] == 'y':
        print(item[0])
        print(item[0][-2:])


