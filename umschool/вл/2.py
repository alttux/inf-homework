L = "205198"
res = 0

for i in range(1, len(L)): # перебор разделения
    P1, P2 = int(L[:i]), int(L[i:]) # P1 = S + M,  P2 = S - N
    if P1 < P2: #невозрастание проверка
        P1, P2 = P2, P1
    # перебор n. Выражаем: M + N = P1 - P2,  S = P2 + N
    for N in range(10):
        M = (P1 - P2) - N
        S = P2 + N
        if N <= 9 and M <= 9:
            if 100 * N <= S <= 100 * M: # сумма 100 цифр, каждая от N до M
                if 99 * N + M <= S <= 99 * M + N: # проверка
                    if  S > res: # наибольшее
                        res = S

print(res)   # 199
