import moeda

p = float(input('Digite o preço \033[32mr$\033[m: '))
print(f'A metade de \033[1;32mr$\033[m{p} é \033[32mr$\033[m{moeda.metade(p)} ')
print(f'O dobro de \033[1;32mr$\033[m{p} é \033[32mr$\033[m{moeda.dobro(p)}')
print(f'Aumentando em 10%, temos \033[32mr$\033[m{moeda.aumentar(p, 10)}')
print(f'Diminuindo o preço em 15% temos \033[32mr$\033[m{moeda.diminuir(p, 15)}')
