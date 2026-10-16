f = open('5.txt')
data = [x.strip() for x in f.readlines() if all(zap not in x for zap in 'EFGHIJKLMNOPQRSTUVWXYZ') and x[0] != '0']
print(data)
c = 0
for n in data:
    if int(n, int(max(n), 16)+1) % 15 == 0:
        c+=1

print(c)