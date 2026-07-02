from ipaddress import *

net = ip_network('167.128.120.83/255.255.255.224', 0)
print(net[-2])