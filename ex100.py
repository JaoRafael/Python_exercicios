from random import randint
from time import sleep


def sorteia(lista):
    print('\033[1;30m-=\033[m'*35)
    print('\033[37mSorteando 5 valores da lista\033[m...')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'\033[1;36m{n}\033[m\033[1;35m->\033[m ', end='')
        sleep(0.5)
    print('\033[31mFIM\033[m')


def sumpar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores \033[4;34mPares\033[m da lista \033[33m{lista}\033[m temos o total de \033[1;34m{soma}\033[m')
    print('\033[1;30m-=\033[m'*35)
numeros = []
sorteia(numeros)
sumpar(numeros)