time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'NS':
            break
        print('ERRO!! Responda apensa S ou N. ')
    if resp == 'N':
        break
print('\033[1m-=\033[m'*25)

print('\033[31mcod\033[m ',end='')
for i in jogador.keys():
    print(f'\033[33m{i:<15}\033[m', end='')
print()
#Cabeçalho

print('\033[32m~\033[m'*50)
for k, v in enumerate(time):
    print(f'\033[31m{k:>2}\033[m- ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('\033[32m~\033[m'*50)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'ERRO!! Não existe jogador com o código {busca}!')
    else:
        print(f'    LEVANTAMENTO DO JOGADOR \033[31m{time[busca]["nome"]}\033[m: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('\033[32m~\033[m'*50)

print('\033[1m>>>\033[m  Volte Sempre  \033[1m<<<\033[m')