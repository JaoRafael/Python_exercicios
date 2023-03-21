casa = float(input('Qual o valor da casa: R$'))
sal = float(input('Qual o seu sálario: R$'))
ano = int(input('Em quantos anos vc quer financiar? '))
#primeira parte
parcela = casa / (ano * 12)
min = sal * 30 / 100
#segunda parte
print(f'Para pagar uma casa de R${casa:.2f}, em {ano} anos, a parcela será de {parcela:.2f}')
if parcela <= min:
    print('Emprestimo APROVADO!!')
else:
    print('Emprestimo NEGADO!')