from ipaddress import *

net = ip_network('181.165.17.108/255.255.192.0', 0)
c = 0
for ip in net:
    if f"{ip:b}".count('0')%9==0:
        c+=1
print(c)