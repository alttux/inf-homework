with open('5.txt') as f:
    count = 0

    for l in f:
        s = sorted(map(int, l.split()))
        c = [x for x in s if x%2==0]
        u = [x for x in s if x%2==1]
        if len(set(s)) == len(s):
            if len(u)>len(c):
                if sum(u)<sum(c):
                    count += 1


print(count)

# 303
