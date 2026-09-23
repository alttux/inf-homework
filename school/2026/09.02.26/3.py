from itertools import permutations
with open('3.txt') as f:
    count = 0
    for l in f:
        s = sorted(map(int, l.split()))
        if s[-2] ** 2 > s[0] * s[-1]:
            for j in permutations('0123', 4):
                if s[int(j[0])] * s[int(j[1])] == s[int(j[2])] * s[int(j[3])]:
                    count += 1
                    break

print(count)

# 13