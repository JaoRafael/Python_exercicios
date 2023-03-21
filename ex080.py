valores = []
for v in range(0, 5):
    num = int(input('Digite um valor: '))
    if v == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista... ')
                break
            pos += 1
print('\033[31m=-\033[m'*35)
print(f'Os valores digitados em ordem foram {valores}')
