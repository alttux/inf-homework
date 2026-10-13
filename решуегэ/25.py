for q1 in range(10):
    for q2 in range(10):
        n = int(f"12345{q1}7{q2}8")
        if n % 23 == 0:
            print(n, n // 23)