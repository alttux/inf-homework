with open('2.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        if s[1]%2==0:
            count += 1
print(count)


# 1519