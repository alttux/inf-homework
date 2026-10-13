cnt = 0
for i in range(30):
    for j in range(i):
        if 2**i + 2**j < 10**9:
            cnt += 1
print(cnt)