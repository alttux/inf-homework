A = [1,1,12,10,10,9,3,2,10,2,9]
B = [A[i] for i in range(len(A)-1) if A[i]==A[i+1]]
print(sum(B))