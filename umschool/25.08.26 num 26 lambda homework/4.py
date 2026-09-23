f = open('6.txt')
n, m, k = map(int, f.readline().strip().split())
data = sorted([list(map(int, x.split())) for x in f], key=lambda p: p[1]-p[0], reverse=True)
in_bus = []
in_bus_every = []
soldouts = 0
for i in range(1, m+1):
    for f in data:
        if (f[1] == i) and (f in in_bus):
            k += 1
    for f in data:
        if k != 0:2
            if f[0] == i:
                k -= 1
                in_bus.append(f)
                in_bus_every.append(f)

    if k == 0:
        soldouts+=1


print(soldouts)

print(data)
print(in_bus_every)
print(len(in_bus_every))