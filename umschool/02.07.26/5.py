n = 6
A = [i // 2 if i % 2 == 0 else (i+1)//2 for i in range(2, n+1)]
print(sum(A))