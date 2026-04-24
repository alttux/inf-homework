with open('7.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        if max(s)**2 > s[0]*s[1]*s[2]*s[3]:
            if (s[4]+s[3])/(s[0]+s[1]+s[2]) > 2:
                count += 1
print(count)
# 10.txt