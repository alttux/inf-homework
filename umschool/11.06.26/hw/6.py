from ipaddress import *
for A in range(32, 1, -1):
    net = ip_network(f'114.75.41.39/{A}', 0)
    net_clone = ip_network(f'114.75.11.61/{A}', 0)
    if net == net_clone:
        c = 0
        for ip in net:
            if f'{ip:b}'.count('1')%2==0:
                c+=1
        print(c)
        break
