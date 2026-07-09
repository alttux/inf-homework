with open('6.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        if (min(s)+max(s))%3==0:
            if abs(s[0]-s[1])==abs(s[2]-s[3]) or abs(s[0]-s[2])==abs(s[1]-s[3]):
                count += 1
print(count)
# 6