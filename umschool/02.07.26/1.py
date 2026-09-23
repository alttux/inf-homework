A = [4, 4, 6, 8, 9, 9, 3, 2, 10, 9, 9]
B = [A[i] for i in range(len(A)-1) if A[i] == A[i+1]]
print(sum(B))