f = open('3.txt')
s = f.readline()
alph = 'HIJKLMNOPQRSTUVWXYZ'

for sym in alph:
    s = s.replace(sym, ' ')

nums = s.split(' ')
print(max(nums, key=len))