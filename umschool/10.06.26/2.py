from ipaddress import *

net = ip_network('176.54.23.0/255.255.192.0', 0)

c = 0

for ip in net:
    if f"{ip:b}".count("1") % 3 == 0:
        c += 1

print(c)
