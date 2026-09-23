n = 10
A = [(i+4)//2 if i % 2 == 0 else (i+3)//2 for i in range(1, n)]
print(sum(A))