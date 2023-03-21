times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atletico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitoria', 'Coritiba', 'Avai', 'Atletico-GO')
print('\033[1;33m~\033[m'*180)
print(f'Lista dos times do Brasileirão: {times}')
print('\033[1;33m~\033[m'*180)
print(f'Os 5 primeiros times são: {times[:5]}')
print('\033[1;33m~\033[m'*86)
print(f'Os 4 ultimos times são: {times[-4:]}')
print('\033[1;33m~\033[m'*74)
print(f'Times em ordem alfabética: {sorted(times)}')
print('\033[1;33m~\033[m'*180)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
print('\033[1;33m~\033[m'*34)