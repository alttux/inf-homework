from ipaddress import *

net = ip_network('196.168.77.128/255.255.255.0', 0)
print(net[1])