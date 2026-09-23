s = 125**27 * 625**81 + 25**9 - 5
cnt = 0
while s > 0:
    if s % 5 == 4:
        cnt+=1
    s //=5

print(cnt)

# 17