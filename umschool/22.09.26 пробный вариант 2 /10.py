from ipaddress import *

net = ip_network('213.146.85.201/255.255.248.0', strict=False)
print(net)
print('---------')
for ip in net:
    print(ip)

# 213.146.87.254
print('---------')
print(213+146+87+254)