from itertools import product

c = 1
for p in product("АЕКНТЦ", repeat=5):
    w = "".join(p)
    if c % 2 == 0 and w[0] not in "АЕК" and w.count("Ц") >= 2:
        print(c)
        break
    c += 1
    