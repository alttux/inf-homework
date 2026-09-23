lfa = []
for na in range(-100, 100):
    for ma in range(na, 100):
        p = range(15, 49)
        q = range(30, 76)
        if all( (x in p) <= (not((x in q) and (x not in range(na, ma))) or not(x in p)) for x in range(-100, 100)):
            # print(abs(na-ma))
            lfa.append(abs(na-ma)-1)

print(min(lfa))