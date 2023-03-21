valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
valor.sort(reverse=True)
print(f'Você digitou {len(valor)} valores \nOs valores digitados foram {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')