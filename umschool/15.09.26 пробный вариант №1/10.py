from ipaddress import *

ip_net = ip_network('176.219.87.213/255.255.240.0', strict=False)
ip_ne2 = ip_network('176.219.80.0/255.255.240.0')
print(ip_net)
print(ip_net==ip_ne2)
print(176+219+80+0)