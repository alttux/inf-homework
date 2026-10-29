def task(s, e, d):
    if s > e or s == 30:
        return 0
    if s == e:
        return 1
    return task(s+d, e, d) + task(s*2, e, d)
c = 0
for i in range(1,62):
    c += (task(1,12,i)*task(12,60,i))

print(c)