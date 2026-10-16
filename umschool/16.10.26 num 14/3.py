c=0
s = 17**140 - 51**73 + 5**267
while s > 0:
    if s%4 == 1:
        c+=1
    s//=4

print(c)