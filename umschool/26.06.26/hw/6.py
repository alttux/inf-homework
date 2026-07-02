for x in sorted('1234567890qwertyuiopasdfghjklzxcvbnm')[:18]:
    s1 = f'AB5{x}3'
    s2 = f'EF{x}13'
    s = int(s1, 18) + int(s2, 18)
    if s % 17 == 0:
        print(x, s//17)

# 157278