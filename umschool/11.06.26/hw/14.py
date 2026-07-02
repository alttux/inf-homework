from ipaddress import *

net = ip_network('111.1.234.205/255.255.248.0', 0)
c = 0
for ip in net:
    print(ip)
    print(f'{ip:b}')
    print(f'{ip:b}'[:8], f'{ip:b}'[8:16], f'{ip:b}'[16:24], f'{ip:b}'[24:32])
    if (f'{ip:b}'[:8].count('0')%2 != f'{ip:b}'[8:16].count('0')%2 ) and \
            (f'{ip:b}'[8:16].count('0')%2 != f'{ip:b}'[16:24].count('0')%2) and \
            (f'{ip:b}'[16:24].count('0')%2 != f'{ip:b}'[24:32].count('0')%2):
        c+=1

print(c)