from datetime import date
atual = date.today().year
nasc = int(input('Qual ano vc nasceu: '))
idade = atual - nasc
if idade == 18:
    print('Você tem que se alistar \033[31mIMEDIATAMENTE\033[31m!!!')
elif idade < 18:
    print(f'Ainda faltam \033[36m{18-idade}\33[m anos para o alistamento \nSeu alistamento será em \033[33m{atual+(18-idade)}\033[m')
else:
    print(f'Você já deveria ter se alistado há \033[36m{idade-18}\033[m anos \nSeu alistamento foi em \033[33m{atual-(idade-18)}')
