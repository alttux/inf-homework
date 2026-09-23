A = [2,1,10,3,4,5,11,10,7,2]
s = sum(A)
for i in range(len(A)):
    if (A[i]%2!=0) and (A[i]<6):
        s = s-A[i]
print(s)