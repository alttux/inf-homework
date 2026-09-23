c = 0
f = open('9.txt')
for l in f:
    s = list(map(int, l.strip().split()))
    # print(s)
    if len(s) == len(set(s)) and ((2*(min(s)+max(s))) > (sum(s)-min(s)-max(s))):
        c+=1
        print(s)
print(c)