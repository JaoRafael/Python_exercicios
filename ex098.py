from time import sleep


def contador(i, f, p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print('\033[1;33m-=\033[m' * 30)
    print(f'Contagem de \033[32m{i}\033[m até \033[31m{f}\033[m de \033[36m{p}\033[m em \033[36m{p}\033[m')
    sleep(0.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'\033[1;37m{cont}\033[m\033[1;36m->\033[m ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('\033[31mFIM\033[m')
    else:
        cont = i
        while cont >= f:
            print(f'\033[1;37m{cont}\033[m\033[36m->\033[m ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('\033[31mFIM\033[m')
    print('\033[1;33m-=\033[m'*30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!!')
inicio = int(input('\033[32mInício\033[m:  '))
fim = int(input('\033[31mFim\033[m:  '))
passo = int(input('\033[37mPasso\033[m:  '))
contador(inicio, fim, passo)
