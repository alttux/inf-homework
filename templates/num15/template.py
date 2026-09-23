for A in range(1, 1000):
    if all((x%A==0) <= (x%25!=0 or x%16==0) for x in range(1, 1001)):
        print(A)
        break