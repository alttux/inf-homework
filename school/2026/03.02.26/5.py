with open('5.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        if sum(s) > 100:
            count += 1

print(count)

# 2499