with open('17.txt') as f:
    a = [int(x) for x in f]

min_p = min(x for x in a if x > 0 and x % 33 == 0)

c = 0
m_s = -float('inf')

for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    if x != y and abs(x - y) % min_p == 0:
        c += 1
        m_s = max(m_s, x + y)

print(c, m_s)