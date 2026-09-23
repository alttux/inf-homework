from ipaddress import *

net = ip_network('213.232.128.145/255.255.128.0', 0)
c = 0
for ip in net:
    if f"{ip:b}".count('0') % 5 == 0:
        c += 1
print(c)