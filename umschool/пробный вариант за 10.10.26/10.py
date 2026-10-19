from ipaddress import *

# from templates.num_ip.template6 import net_clone

net = ip_network('173.94.214.57/255.255.240.0', strict=False)

for i in net:
    print(i)

print(173+94+223+255)