from random import randint
print('\033[1;33m JOGO DO PAR OU IMPAR!!!')
print('\033[30m~\033[m' * 30)
V = 0
while True:
    player = int(input('\033[1m>>>\033[m Digite um valor: '))
    cpu = randint(1, 10)
    total = player + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? \033[1m[P/I]\033[m: ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {cpu}. Total de {total}', end=' ')
    print('Deu \033[33mPAR\033[m' if total % 2 ==0 else 'Deu \033[33mIMPAR\033[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você \033[1;32mVENCEU\033[m!!!')
            V += 1
        else:
            print('Você \033[1;31mPERDEU\033[m!!!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você \033[1;32mVENCEU\033[m!!!')
            V += 1
        else:
            print('Você \033[1;31mPERDEU\033[m!!!')
            break
    print('Vamos jogar Novamente... ')
    print('\033[30m~\033[m' * 30)
print(f'\033[4;35mG A M E  O V E R ! !\033[m Você venceu \033[33m{V}\033[m vezes.')
