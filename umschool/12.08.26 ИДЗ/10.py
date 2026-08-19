from ipaddress import *

print(list(ip_network('167.128.120.83/255.255.255.224', 0))[-5:])