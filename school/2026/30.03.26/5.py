min_diff = 1000
best_N = 0
for N in range(1, 100):
    B = bin(N)[2:]
    if N % 3 == 0:
        lt = B[-3:]
        R_bin = B + lt
    else:
        rem = N % 3
        ab = bin(rem * 3)[2:]
        R_bin = B + ab
    R = int(R_bin, 2)
    diff = abs(R - 130)
    if diff < min_diff:
        min_diff = diff
        best_N = N
    elif diff == min_diff and N > best_N:
        best_N = N

print(best_N)
