for G in range(100, 0, -1):
    if all(
            (2*f+h!=70) or (f<h) or (G<f)
        for f in range(0,100)
        for h in range(0,100)
    ):
        print(G,end=" ")
        break