#134?3?
print(*[f'{i} | {i//63}' for i in range(134030, 134939+1) if i%63==0 and str(i)[-2]=='3'])