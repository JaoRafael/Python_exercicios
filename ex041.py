from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano que vc nasceu? '))
idade = atual - nasc
print(f'O Atleta tem {idade} anos')
if idade <= 9:
    print('Classificação MIRIM.')
elif idade <= 14:
    print('Classificação INFANTIL.')
elif idade <= 19:
    print('Classificação JUNIOR.')
elif idade <= 25:
    print('classificação SÊNIOR.')
else:
    print('Classificação MASTER.')