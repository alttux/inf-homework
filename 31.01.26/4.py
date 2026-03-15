with open('4.txt') as f:
    count = 0

    for l in f:
        s = sorted(map(int, l.split()))
        # print(s)
        if min(s)*6 < sum(s)-min(s):
            if  min(s)*max(s) > s[1]*s[2]:
                count += 1

print(count)


# 118
