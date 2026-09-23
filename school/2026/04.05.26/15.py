# Описываем отрезки
P = lambda x: 15 <= x <= 30
Q = lambda x: 60 <= x <= 80


def F(x, A_start, A_end):
    A = A_start <= x <= A_end
    left = not (not A or P(x))
    right = not (not A or not Q(x))
    return not left or right


coords = [15, 30, 60, 80]
ans = []

for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        A_start, A_end = coords[i], coords[j]
        if all(F(x / 10, A_start, A_end) for x in range(0, 1000)):
            ans.append(A_end - A_start)

print(max(ans))