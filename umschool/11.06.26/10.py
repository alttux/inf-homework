from ipaddress import *
for n in range(0,9):
    A = int(('1'*n + '0'*(8-n)), 2)
    net = ip_network(f'255.224.33.160/255.255.{A}.0', 0)
    if all((f'{ip:b}'[:16].count('1') >= f'{ip:b}'[16:].count('1')) for ip in net):
        print(A)
# a = '1234'
# print(a[:2], a[2:])