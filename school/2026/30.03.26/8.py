alph = sorted('цитрус')

count = 0
last_pos = 0

for n1 in alph:
    for n2 in alph:
        for n3 in alph:
            for n4 in alph:
                for n5 in alph:
                    count += 1
                    w = f'{n1}{n2}{n3}{n4}{n5}'
                    if w.count('и') == 2 and 'иц' not in w and 'ци' not in w:
                        last_pos = count

print(last_pos)
