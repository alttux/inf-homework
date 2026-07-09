import ipaddress
from ipaddress import ip_network

net = ip_network('68.203.243.87/19', 0)
print(net[-2])
print(68+203+255+254)