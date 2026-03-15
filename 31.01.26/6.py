with open('6.txt') as f:
    count = 0
    k = 0
    for l in f:
        k+=1
        s = sorted(map(int, l.split()))
        p = [x for x in s if s.count(x) > 1]
        np = [x for x in s if s.count(x) == 1]
        if len(set(p))==2 and len(p)==4 and len(np)==3:
            if max(s) not in p:
                print(k)
                print(sum(s))
                break



# 261
