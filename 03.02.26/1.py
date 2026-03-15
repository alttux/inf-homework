with open('1.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        if s[2]-s[0] > s[1]:
            count += 1
print(count)


# 1422