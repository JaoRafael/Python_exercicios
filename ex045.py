from random import randint
from time import sleep
itens = ('\033[37mPedra\033[m', '\033[34mPapel\033[m', '\033[30mTesoura\033[m')
cpu = randint(0, 2)
print('''\033[1mSuas opções são:\033[m
[ 0 ] \033[37mPEDRA\033[m
[ 1 ] \033[34mPAPEL\033[m
[ 2 ] \033[30mTESOURA\033[m''')
player = int(input('Qual é a sua jogada? '))
print('\33[36mJO\33[m')
sleep(1)
print('\033[36mKEN\033[m')
sleep(1)
print('\033[36mPO !!!\033[m')
sleep(1)
print('\033[1;35m-=\033[m'* 11)
print(f'Computador jogou {itens[cpu]}')
print(f'Você jogou {itens[player]}')
print('\033[1;35m-=\033[m'*11)
if cpu == 0:
    if player == 0:
        print('\033[33MEMPATE\033[m !!')
    elif player == 1:
        print('\033[32mVOCÊ GANHOU\033[m !!')
    elif player == 2:
        print('\033[31mVOCÊ PERDEU\033[m !!!')
    else:
        print('JOGADA INVALIDA!')
elif cpu == 1:
    if player == 0:
        print('\033[31mVOCÊ PERDEU\033[m !!!')
    elif player == 1:
        print('\033[33mEMPATE\033[33m !!')
    elif player == 2:
        print('\033[32mVOCÊ GANHOU\033[m !!')
    else:
        print('\033[1mJOGADA INVÁLIDA\033[m !')
elif cpu == 2:
    if player == 0:
        print('\033[32mVOCÊ GANHOU\033[m !!')
    elif player == 1:
        print('\033[31mVOCÊ PERDEU\033[m !!!')
    elif player == 2:
        print('\033[33mEMPATE\033[m !!')
else:
    print('Jogada inválida')
