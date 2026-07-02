from ipaddress import *

net = ip_network('192.168.32.176/255.255.255.240',0)
c = 0
for ip in net:
    if not(f'{ip:b}'.count('1') % 2 == 0):
        c +=1

print(c)