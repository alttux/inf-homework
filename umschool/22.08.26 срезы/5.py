n = []
for i in range(10000, 60000, 4):
    if '2' in str(i)[:3] and '5' in str(i)[2:] and '25' not in str(i)[1:4] and '52' not in str(i)[1:4]:
     n.append(str(i))

print(n[0]+n[-1])
