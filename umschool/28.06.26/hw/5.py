s = 5**172 + 4**347 - 8**93
c = 0
while s > 0:
    if s % 4 == 0:
        c += 1
    s //= 4

print(oct(c)[2:])