import ipaddress
net = ipaddress.ip_network('217.9.142.131/255.255.192.0', strict=False)
addr = str(net.network_address)
print(addr)