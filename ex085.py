lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite {c}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-='*30)
lista[0].sort()
lista[1].sort()
print(f'Todos o valores são: {lista} '
      f'\nOs valores pares são: {lista[0]} '
      f'\nOs valores impares são: {lista[1]}')
