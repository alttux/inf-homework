for x in sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')[:19]:
    s1 = f'11A{x}3'
    s2 = f'12{x}345'
    s = int(s1, 19) + int(s2, 19)
    if s % 14 == 0:
        print(x, s//14)
        break

# 208569