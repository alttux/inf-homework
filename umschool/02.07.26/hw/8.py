A = [4,2,4,4,15,12,3,2,4,6]
B = [A[i] for i in range(1, len(A)) if A[i] != A[0]]
cnt = 0
print(len(B))