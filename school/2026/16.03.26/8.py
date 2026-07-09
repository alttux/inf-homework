alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
lst = []

for x in alph[:19]:
    n1 = f'98{x}79731'
    n2 = f'36{x}14'
    n3 = f'73{x}4'
    a = int(n1, 19) + int(n2, 19) + int(n3, 19)
    if a%18==0:
        print(x, a/18)

# 467926139