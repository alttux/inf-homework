with open('3.txt') as f:
    count = 0

    for l in f:
        s = sorted(map(int, l.split()))
        if len(set(s)) == len(s):
            if (max(s)+min(s))*3 <= (sum(s)-max(s)-min(s))*2:
                count += 1

print(count)

# 853
