from time import sleep


def maior(*num):
    cont = maior = 0
    print('\033[1;30m-\033[m\033[1;33m=\033[m'*30)
    print('\033[1mAnalisando os valores passados...\033[m')
    sleep(0.5)
    for valor in num:
        print(f'\033[1;36m{valor}\033[m\033[1;35m->\033[m ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print('\033[1;31mFIM\033[m')
    print(f'Foram infomados \033[1;33m{cont}\033[m valores ao todo.')
    print(f'O \033[4mmaior\033[m valor informado foi \033[1;34m{maior}\033[m.')
    sleep(0.5)


maior(2, 9, 4, 6, 1, 10)
maior(7, 3, 1)
maior(7, 5)
maior()
