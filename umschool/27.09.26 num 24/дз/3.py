s = open('cb2ba2f0-318e-40d3-a867-9a92e8b32f2e_24.3.txt').readline().replace('E', 'I').replace('O', 'I').replace('K', 'M')
for i in range(100):
    if 'MI'*i in s:
        print(i)