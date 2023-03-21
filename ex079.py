valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado!')
    else:
        print('Valor Duplicado! não adicionado')
    resp = str(input(('Deseja continuar? [S/N] '))).strip().upper()[0]
    if resp in 'Nn':
        break
    if resp not in 'NnSs':
        print('Resposta inválida!!')
        break
valores.sort()
print(f'Você digitou os valores {valores}')
