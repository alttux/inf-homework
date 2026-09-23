c = 0
f = open('9.txt')
for l in f:
    s = sorted(list(map(int, l.strip().split())), reverse=True)
    print(s)

    if len(set(s)) == len(s) or (s[0]+s[1]) > 2*(sum(s)-s[0]-s[1]):
        c+=1

print(c)