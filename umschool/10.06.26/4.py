from ipaddress import *

c = 0
for A in range(256):
    net = ip_network(f'207.0.{A}.163/255.255.255.192', 0)
    for ip in net:
        if (f"{ip:b}"[16:].count('0') < f"{ip:b}"[:16].count('0')) == False:
            break
    else:
        c += 1

print(c)
    