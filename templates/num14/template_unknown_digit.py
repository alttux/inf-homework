from string import digits, ascii_uppercase

# Задание 14: поиск неизвестной цифры x в числе в системе счисления с основанием > 10
# Буквы A=10, B=11, ... используются как цифры

alph = digits + ascii_uppercase[:9]  # '0123456789ABCDEFGHI' — для основания 19

for x in alph:
    s1 = f'98{x}79641'
    s2 = f'36{x}14'
    s = int(s1, 19) + int(s2, 19)
    if s % 18 == 0:
        print(x, s // 18)
        break
