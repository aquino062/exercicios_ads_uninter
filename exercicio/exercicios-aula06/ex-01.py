palavras = ('mario', 'luigi','peach','yoshi','bowser')

for i in palavras:
    print('\nPalavras: {}. vogais:  '.format(i.upper()), end='')
    for j in i:
        if j.lower() in 'aeiou':
            print(j.upper(), end=' ')
