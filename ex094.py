cambada = []
pessoa = {}
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!! por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cambada.append(pessoa.copy())

    while True:
        resp = str(input('Segue o baile? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! Responda apenas S ou N.')

    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(cambada)} pessoas cadastradas.')
media = soma / len(cambada)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='= ')

for p in cambada:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média:', end='')

for p in cambada:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('>>> ACABOOOOUUU <<<')
