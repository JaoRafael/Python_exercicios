preco = float(input('Preço das suas compras: '))
print('''\033[1;33mFORMAS DE PAGAMENTO\033[m
[ 1 ] À vista Dinheiro/Pix
[ 2 ] À vista no Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')
opcao = int(input('Digite a opção escolhida: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS! ')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc} de {parcela:.2f} COM JUROS! ')
else:
    total = 0
    print('\033[1;31m[ ERRO!! ]\033[m Opção Inválida!!')
print(f'Sua compra de R$\033[33m{preco:.2f}\033[m vai custar no final R$\033[32m{total:.2f}\033[m no final')