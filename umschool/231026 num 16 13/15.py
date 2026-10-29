for i in range(100):
    n = '1'*97 + '0'*i
    if int(n,2) < 2**100:
        print(int('1'*97, 2))
        print(int(n,2))
# print(2**100)