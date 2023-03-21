vel = float(input('Qual é a sua velocidade? '))
if vel > 80:
    print(f'MULTADO! você ultrapassou o limite que é 80km/h \nVocê deve pagar uma multa de R${(vel-80)*7:.2f}')
else:
    print('Tenha um bom dia! Dirija com segurança')