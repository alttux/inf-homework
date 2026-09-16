from ipaddress import *

# Задание: найти позицию IP-адреса в списке хостов сети (нумерация с 1)

ip_addr = '114.126.104.124'
net = ip_network(f'{ip_addr}/255.255.255.240', 0)

# hosts() возвращает только хосты (без сетевого и широковещательного)
# index() возвращает позицию с 0, +1 для нумерации с 1
print(list(net.hosts()).index(IPv4Address(ip_addr)) + 1)
