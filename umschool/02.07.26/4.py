A = [4, 7, 3, 8, 5, 0, 1, 2, 9, 6]
B = [i for i in range(1, len(A)) if A[i] <= A[0]]
print(len(B))