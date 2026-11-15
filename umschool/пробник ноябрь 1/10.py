from ipaddress import *


net = ip_network('203.117.94.38/255.255.192.0', strict=False)

for i in net:
    print(i)

print(203+117+127+254)