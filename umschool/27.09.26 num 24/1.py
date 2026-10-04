s = open("24.1.txt").readline()
for i in range(100, 1, -1):
    if 'Q'*i in s:
        print(i)
        break

