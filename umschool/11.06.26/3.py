from ipaddress import *

net = ip_network("112.208.0.0/255.255.128.0")

cnt = 0

for ip in net:
    if f'{ip:b}'.count('1') % 11 == 0:
        cnt += 1

print(cnt)