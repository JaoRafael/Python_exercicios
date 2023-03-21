tot18 = toth = totm = 0
print('\033[1;30m-\033[m'*30)
while True:
    idade = int(input('\033[1m>>>\033[m Digite a Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[1m>>>\033[m Sexo \033[1m[M/F]\033[m: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[1m>>>\033[m Quer Continuar? \033[1m[S/N]\033[m: ')).strip().upper()[0]
        print('\033[1;30m-\033[m' * 30)
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: \033[33m{tot18}\033[m '
      f'\nAo total temos \033[33m{toth}\033[m homens cadastrados '
      f'\nE temos \033[33m{totm}\033[m Mulheres com menos de 20 anos.')