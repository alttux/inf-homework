def calculate_R(N):
    nb = bin(N)[2:]  
    ce = 0  
    co = 0   
    for index, bit in enumerate(nb):
        position = index + 1  
        if position % 2 == 0:  
            if bit == '1':
                ce += 1
        else:  
            if bit == '0':
                co += 1
    R = abs(ce - co)
    return R
for N in range(2, 1000):
    if calculate_R(N) == 4:
        print(N)
        break