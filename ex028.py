from random import randint #seleciona um numero aleatorio do tipo inteiro
from time import sleep
cpu = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um Número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
player = int(input('Em que Número eu estou pensando? '))
print('Processando...')
sleep(3)
if player == cpu:
    print('Parabens você ACERTOU!!')
else:
    print(f'Você PERDEU eu pensei no Número {cpu} e não no Número {player}')
