for n in range(6, 36):
    a = 7 ** 500 - (5 * n + 3)
    if a  % 6 == 0:
        print(n)
        break
# 8