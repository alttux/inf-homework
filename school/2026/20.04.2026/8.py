for G in range(1,100):
    if all(
            (f+2*h<G) or (h<f)or (h>22)
        for h in range(0,100)
        for f in range(0,G)
    ):
        print(G)
        break