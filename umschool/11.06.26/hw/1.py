from ipaddress import *

net = ip_network('222.78.233.34/255.255.240.0', 0)

print(net[0])