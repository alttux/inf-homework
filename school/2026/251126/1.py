from itertools import product


for num, word in enumerate(product(sorted('WORLD'), repeat=5), 1):
    word = ''.join(word)
    if word[0] == 'W':
        print(num)
