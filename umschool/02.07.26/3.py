A = [7, 3, 4, 8, 6, 9, 5, 2, 0, 1]
j = 0
for k in range(2, 10):
    if A[k] <= 4:
        j += k

print(j)