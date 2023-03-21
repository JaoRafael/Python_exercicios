sexo = str(input('Digite o seu sexo [F/M] ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos, Por favor digite seu sexo: ')).upper()[0].strip()
print(f'Sexo {sexo} registrado com sucesso!')
