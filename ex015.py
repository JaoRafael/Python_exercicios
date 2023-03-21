dias = int(input('Quantos dias alugados? '))
per = float(input('Quantidade de Km percorridos? '))
print(f'O total a pagar é de R${(dias*60)+(per*0.15):.2f}')