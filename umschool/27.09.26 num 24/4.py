s = open('24.4.txt').readline().replace('U', 'A').replace('S', 'R').replace('T', 'R')
for i in range(100, 1, -1):
    if 'AR'*i in s:
        print(i)
        break