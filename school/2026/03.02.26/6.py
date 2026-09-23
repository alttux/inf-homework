with open('6.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        if sum(s)%18==0:
            count += 1

print(count)

# 923