import itertools
alph = "ИГОРЬ"
ar = itertools.product(alph, repeat=8)
lst = []
for i in ar:
    lst.append(list(i))
count = 0
for j in lst:
    if j.count("О") == 1 and j.count("Ь") == 1 and j[0] != "Ь":
        count += 1
print(count)