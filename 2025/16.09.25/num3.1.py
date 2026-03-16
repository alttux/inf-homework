import itertools

# функция F по формуле: ((y → z) ∨ (¬x ∧ w)) ≡ (w ≡ z)
def F(x, y, z, w):
    impl_yz = (not y) or z
    left = impl_yz or ((not x) and w)
    right = (w == z)
    return int(left == right)

# строки таблицы (с неизвестными = None)
# порядок: Перем1, Перем2, Перем3, Перем4, F
rows = [
    [None, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 1, None, None, 1]
]

vars_names = ['x','y','z','w']

# перебираем все перестановки соответствия
for perm in itertools.permutations(vars_names):
    ok = True
    for row in rows:
        mapping = {perm[i]: row[i] for i in range(4)}
        # перебираем возможные варианты для None
        options = [mapping.copy()]
        for var, val in mapping.items():
            if val is None:
                new_options = []
                for opt in options:
                    for b in (0,1):
                        opt2 = opt.copy()
                        opt2[var] = b
                        new_options.append(opt2)
                options = new_options

        # проверим, что хотя бы один вариант подходит
        if not any(F(opt['x'], opt['y'], opt['z'], opt['w']) == row[4] for opt in options):
            ok = False
            break

    if ok:
        print("Подходит:", ''.join(perm))
