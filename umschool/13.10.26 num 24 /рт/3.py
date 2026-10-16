f = open('24_3.txt')
s =  f.readline()

for sym in 'GHIJKLMNOPQRSTUVWXYZ':
    s = s.replace(sym, ' ')

hexes = s.split(' ')

print(len(max(hexes, key=len)))