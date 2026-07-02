s = 1024**789 + 256**678 - 64**567
cnt = 0
while s > 0:
    if s % 5 == 4:
        cnt += 1
    s//=5

print(cnt)

# 662