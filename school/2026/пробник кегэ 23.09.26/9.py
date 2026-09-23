with open('9.csv') as f:
    for line in f:
        lst = list(map(int, line.strip().split(';')))
        if len(set(lst)) == 5:
            mx, mn = max(lst), min(lst)
            if 2 * (mx + mn) > sum(lst) - mx - mn:
                print(sum(lst))
                break