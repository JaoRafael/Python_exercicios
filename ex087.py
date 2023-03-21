matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3): # for feito para linha pq a coluna é fixa, a linha vai variar!
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3): # for feito para colna pq a linha é fixa, a coluna vai variar!
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        # o maior elemente é sempre o primeiro, se a coluna for a primeira é sinal de que ele é o maior,
        # se nao for a primeira eu faço uma comparação com o maior valor, se ele for o maior ai troca
        mai = matriz[1][c]
print(f'O maior número da segunda linha é {mai}')