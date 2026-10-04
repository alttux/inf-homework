s = open('24.5.txt').readline().replace('FJN', 'JFN')
for i in range(100, 1, -1):
    if 'JFN'*i in s:
        print(i)