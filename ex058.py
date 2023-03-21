from random import randint
cpu = randint(0, 10)
print('\033[1mOlá sou seu Computador... '
      '\nAcabei de pensar em um número entre 0 e 10. '
      '\nSeráse que vc adivinha? \033[m')
acertou = False
palpite = 0
while not acertou:
    player = int(input('Qual é o seu palpite: '))
    palpite += 1
    if player == cpu:
        acertou = True
    else:
        if player < cpu:
            print('Mais... Tente outra vez: ')
        else:
            print('Menos... Tente outra vez: ')
print(f'\033[1;32mAcertou\033[m com \033[1m{palpite}\033[m tentativas!')
