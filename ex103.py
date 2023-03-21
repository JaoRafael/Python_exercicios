def ficha(jog='\033[31m<Desconhecido>\033[m', gol=0):
    print(f'O jogador \033[33m{jog}\033[m fez \033[34m{gol}\033[m gol(s) no campeonato')
    print('\033[1;37m-\033[m'*52)


print('\033[1;37m------->\033[m  \033[32mFicha de jogadores\033[m  \033[1;37m<-------\033[m')
n = str(input('Digite o nome do jogador: '))
g = str(input('Digite o número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
