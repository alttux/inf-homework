s = 234**123 + 32**12 - 32
cnt = 0
while s > 0:
    if s % 4 == 3:
        cnt+=1
    s //= 4

print(cnt)

# 136