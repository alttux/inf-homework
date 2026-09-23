alph = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')


for x in range(0,10):
    n1 = f'{x}b09'
    n2 = f'{x}8e8'
    a = int(n1, 17) + int(n2, 15)
    if a%155==0:
        print(x, a//155)
# 194