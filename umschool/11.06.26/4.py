from ipaddress import *

net = ip_network('156.128.0.227/255.255.255.248', 0)

print(int(f'{ip_address('156.128.0.227'):b}', 2) - int(f'{net.network_address:b}', 2))