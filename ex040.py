n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'Tirando {n1} e {n2} a média é {media:.1f} \nO Aluno esta \33[32mAPROVADO\033[m !!!')
elif 7 > media >= 5:
    print(f'Tirando {n1} e {n2} a média é {media:.1f} \nO Aluno está de \033[33mRECUPERAÇÃO\033[m !!!')
else:
    print(f'Tirando {n1} e {n2} a média é {media:.1f} \nO Aluno está \033[31mREPROVADO\033[m !!!')
