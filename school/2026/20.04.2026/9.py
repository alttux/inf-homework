for G in range(0,500):
    if all(
            (f>=12) or (3*f<h) or (f*h<G)
        for f in range(0,500)
        for h in range(0,500)

    ):
      print(G)
      break