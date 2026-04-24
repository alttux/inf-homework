alph = sorted('АВТОР')
cnt = 0
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                cnt += 1
                if a+b+c+d=='ВАТА':
                    print(cnt)
# 146