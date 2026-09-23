m_z = -1
ans = 0
for x in range(1, 2031):
    v = 5**150 + 5**100 - x
    c = 0
    while v > 0:
        if v % 5 == 0:
            c += 1
        v //= 5
    if c >= m_z:
        m_z = c
        ans = x
print(ans)