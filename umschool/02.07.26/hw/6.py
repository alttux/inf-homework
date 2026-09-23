n = 8
A = [i + 4 if i % 2 == 0 else i + 5 for i in range(2, n + 1)]
print(sum(A))
