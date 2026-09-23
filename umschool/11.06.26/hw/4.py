from ipaddress import *
ip_addr = '114.126.104.124'
net = ip_network(f'{ip_addr}/255.255.255.240', 0)

print(list(net.hosts()).index(IPv4Address('114.126.104.124'))+1)