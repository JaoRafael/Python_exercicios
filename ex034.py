sal = float(input('Qual é o salário do funcionario? R$:'))
if sal <= 1250:
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${sal+(sal*15/100):.2f}.')
else:
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${sal+(sal*10/100):.2f}.')
