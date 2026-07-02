n = 3
A = [i + 2 if i % 2 == 0 else i + 3 for i in range(2, n + 1)]
print(sum(A))
