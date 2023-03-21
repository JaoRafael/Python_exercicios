nome = str(input('Digite seu Nome Completo: ')).strip()
separa = nome.split()
print(f'Analisando seu Nome...'
      f'\nEle em letras maiúsculas é {nome.upper()}'
      f'\nEle em letras minúsculas é {nome.lower()}')
print('Ele tem ao total de {} letras '.format(len(nome)-nome.count(' ')))
print('Seu Primeiro Nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

