from datetime import date
hoje = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Em qual ano a {pessoa}ª pessoa nasceu: '))
    idade = hoje - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao total tivemos \033[32m{totmaior}\033[m pessoas maiores de idade '
      f'\nE também tivemos \033[31m{totmenor}\033[m pessoas menores de idade')


