nome = str(input("Digite seu nome completo ")).strip().split()
print(f'Muito prazer em te conhececer! '
      f'\nSeu primeiro nome é {nome[0]} '
      f'\nSeu ultimo nome é {nome[len(nome)-1]}')
