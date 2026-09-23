from itertools import product, repeat
c = 0
for i in product(sorted("ЕКЛМОТ"), repeat=5):
    i = ''.join(i)
    if i[0] not in 'ЕО' and "ЕЕ" not in i and "КК" not in i and "ЛЛ" not in i and "ММ" not in i and "ОО" not in i and "ТТ" not in i and ((i.count("Е")+i.count("О")) == 2):
        print(i)
        c+=1
print(c)