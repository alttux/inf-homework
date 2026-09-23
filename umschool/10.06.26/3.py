from ipaddress import *

net = ip_network("142.96.56.118/255.255.255.240", 0)
c = 0

for ip in net:
    if f"{ip:b}"[16:].count('1') > f"{ip:b}"[:16].count('1'):
        c += 1

print(c)

# print('101110000'[:4], '101110000'[4:])