from string import digits, ascii_uppercase
alph = digits + ascii_uppercase[:9]
for x in reversed(alph):
    s1 = f'98{x}79641'
    s2 = f'36{x}14'
    s3 = f'73{x}4'
    s = int(s1, 19) + int(s2, 19) + int(s3, 19)
    if s % 18 == 0:
        print(x, s//18)
        break

# 470402599