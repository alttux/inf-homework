with open('3.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        if sum(s) > 2*max(s):
            count += 1

print(count)

# 1538