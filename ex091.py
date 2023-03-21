from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1 -': randint(1, 6),
        'Jogador 2 -': randint(1, 6),
        'Jogador 3 -': randint(1, 6),
        'Jogador 4 -': randint(1, 6)}

ordem = ()
print('-='*15)
print('Valores Sorteados: ')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ordem = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*15)
print('RANKING')
for i, v in enumerate(ordem):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
