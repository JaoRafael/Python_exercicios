somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print(f'\033[7m----- {p}ª PESSOA -----\033[m')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    elif sexo in 'Mn' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de \033[31m{mediaidade}\033[m '
      f'\nO homem mais velho tem \033[34m{maioridadeh}\033[m e se chama \033[37m{nomevelho}\033[m '
      f'\nAo todo são \033[35m{totmulher}\033[m mulheres com menos de \033[35m20\033[m anos' )
