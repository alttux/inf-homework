def algorithm(N):
    binary = bin(N)[2:]
    ones = binary.count('1')
    zeros = binary.count('0')
    result_binary = bin(ones)[2:] + bin(zeros)[2:]
    return int(result_binary, 2)

for N in range(1, 10**7):
    if algorithm(N) == 183:
        binary = bin(N)[2:]
        ones = binary.count('1')
        zeros = binary.count('0')
        print(f"N = {N}, двоичная: {binary}")
        print(f"Единиц: {ones} ({bin(ones)[2:]}), Нулей: {zeros} ({bin(zeros)[2:]})")
        print(f"Склеенное: {bin(ones)[2:] + bin(zeros)[2:]} = {183}")
        break