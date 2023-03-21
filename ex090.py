aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno ['media'] >= 7:
    aluno['Situação'] = 'Aprovado!'
elif 5 <= aluno['media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'REPROVADO!'

print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
