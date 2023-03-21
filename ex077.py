palavras = ('phyton', 'impacta', 'faculdade', 'ensino', 'distancia', 'estudar', 'praticar', 'linguagem')
for p in palavras:
    print(f'\nNa Palavra \033[1m{p.upper()}\033[m temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
