from ipaddress import *

net = ip_network('242.52.23.67/255.255.128.0', 0)
c = 0
for ip in net:
    if f'{ip:b}'[16:].count('1') < 0.5*f'{ip:b}'[:16].count('1'):
        c+=1
print(c)