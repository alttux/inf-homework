c=0
for a in range(96,128):
    for b in range(256):
        if (bin(172).count('1')+bin(16).count('1')+bin(a).count('1')+bin(b).count('1'))%2==0: c+=1
print(c)