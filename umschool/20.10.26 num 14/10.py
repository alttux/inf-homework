from string import digits, ascii_uppercase
f = open("24_2.txt")
s = f.readline()
alph = digits + ascii_uppercase[:...]
cnt = 0
mx = 0
for c in s:
    if c in alph:
        cnt += 1
        mx = max(mx, cnt)
else:
    cnt = 0

print(mx)
3
4
5
6
7
8
9
10
11
13