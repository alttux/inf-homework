from itertools import product, repeat

for num, s in enumerate(product(sorted('ДИКОРС'), repeat=5), 1):
    s = ''.join(s)
    # print(num, s)
    if (num % 2 == 0) and (s[0] not in 'ДИК') and s.count("С") >= 1:
        print(num, s)