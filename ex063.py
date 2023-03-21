print('\033[1;34m-\033[m'*38)
print('\033[1m      Sequência de Fibonacci\033[m')
print('\033[1;34m-\033[m'*38)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('\033[33m~\033[m'*38)
print(f'{t1} \033[1;32m→ \033[m{t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' \033[1;32m→\033[m {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' \033[1;32m→ \033[m\033[31mEND\033[m')
print('\033[33m~\033[m'*38)
