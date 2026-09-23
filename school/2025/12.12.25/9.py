nlst = []

for n in range(1, 1000):
    nb = bin(n)[2:] 
    nb = nb + str(nb.count('1') % 2)  
    nb = nb + str(nb.count('1') % 2)  
    
    r = int(nb, 2)  
    if r > 144:  
        nlst.append(n) # или nlst.append(r)

print(min(nlst))
