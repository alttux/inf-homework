s = open('2c9d676d-2278-41b3-b382-255884b792da_24.6.txt').readline().replace('ANT', 'AN NT').replace('AN', 'NT')
for i in range(100, 1, -1):
    if 'NT'*i in s:
        print(i)
        break