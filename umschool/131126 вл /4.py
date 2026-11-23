c = 0
for l in open('4.txt'):
    s = list(map(int, l.split()))
    ch = [x for x in s if x % 2 == 0] # четные числа из строки
    nch = sorted(x for x in s if x % 2) # нечетные числа в строке

    u1 = len(set(s)) == 5 # условие 1
    u2 = bool(ch) and len(nch) >= 2 and \
         abs(max(ch) - sum(s) / len(s)) > abs(nch[-2] - min(ch))
    # условие 2 ( если есть четные и длина списка нечетных чисел болееравна 2, а дальше проверка условия)

    if u1 + u2 == 1: # проверка условия
        c += 1
print(c)
