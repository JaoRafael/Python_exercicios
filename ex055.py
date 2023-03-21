maior = 0
for pe in range (1, 6):
    peso = float(input(f'Peso da {pe}ª Pessoa: '))
    if pe == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso lido foi de \033[34m{maior}\033[mKg'
      f'\nO menor peso lido foi de \033[33m{menor}\033[mkg')
