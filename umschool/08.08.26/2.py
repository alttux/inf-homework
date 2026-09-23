f  = open('task2.txt')
ips = {}
for s in f:
    ip = s.strip()
    if ip in ips:
        ips[ip]+=1

    else:
        ips[ip] = 1

print(min(ips, key=ips.get), max(ips, key=ips.get))