print('      \033[1mGerador de PA\033[m')
print('\033[1;33m-=\033[m'*16)
first = int(input('>> Digite o primeiro termo: '))
raz = int(input('>> Digite a razão: '))
termo = first
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} \033[1;36m→\033[m ', end='')
        termo += raz
        cont += 1
    print('\033[33mPAUSE\033[m')
    mais = int(input('Quantos termos a mais você uocê quer mostrar: '))
print(f'Progressão Finalizada com \033[31m{total}\033[m termos mostrado.')
