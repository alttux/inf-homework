n = range(3, 26)
m = range(8, 57)
a = list(range(1, 1000))
for x in range(1, 1000):
    if (((x in n) <= (x in m)) <= (x not in a)) == False:
        a.remove(x)

print(a)
# 5