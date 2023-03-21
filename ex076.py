lista =('Caneta', 2.5,
        'Caderno', 10.9,
        'Mochila', 250.,
        'Livro', 35.8,
        'Estojo', 15,
        'Compasso', 9.9,)
print('='*40)
print(f'{"LISTA DE PREÇOS":^40}')
#texto centralizado
print('='*40)
for pos in range(0, len(lista)):
    #vai do 0 até o tamanho da lista
    if pos % 2 == 0:
        #nome do produto sempre na posição par
        print(f'{lista[pos]:.<30}', end='')
        #alinhado o texto a esquerda com pontos
    else:
        print(f'R${lista[pos]:>7.2f}')
        #alinhado o texto a direita com formatação de 2 casas decimais
print('='*40)