from fnmatch import *

# 123*578

for x in range(31, 10**8, 31):
    if str(x)[:3] == '123' and str(x)[-3:] == '578':
        print(f'{x} | {x//31}')
print('---')
for i in range(31, 10**8, 31):
    if fnmatch(str(i), '123*578'):
        print(i, i//31)