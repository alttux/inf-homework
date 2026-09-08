print(*[f'\t{i} | {i // 61}\n' for i in range(23456208, 23456999, 61) if str(i)[-1]=='8'])
