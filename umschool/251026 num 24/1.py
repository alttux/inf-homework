f = open('1.txt','r')
c = 0
for l in f:
    if l.count('AB') > 1 and 1 < l.count('C') <= l.count('AB'):
        c+=1
print(c)