import ipaddress

net = ipaddress.IPv4Interface('189.163.226.71/255.255.255.240')

network_address = str(net.network.network_address)

print(network_address)