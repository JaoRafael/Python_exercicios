print('      \033[1mGerador de PA\033[m')
print('\033[1;33m-=\033[m'*16)
first = int(input('>> Digite o primeiro termo: '))
raz = int(input('>> Digite a razão: '))
termo = first
cont = 1
while cont <= 10:
    print(f'{termo} \033[1;36m→\033[m ', end='')
    termo += raz
    cont += 1
print('\033[31mEND\033[m')