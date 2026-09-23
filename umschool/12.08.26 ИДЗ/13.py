c_0=[]
for x in range(2031):
    a = 8**3000 + 8**300 - x
    ao = oct(a)[2:]
    c_0.append(ao.count('0'))

print(min(c_0))