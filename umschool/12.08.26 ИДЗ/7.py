from ipaddress import *

print(list(ip_network('64.237.228.143/21', 0))[-1])
