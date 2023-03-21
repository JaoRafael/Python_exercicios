def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno de {largura} x {comprimento} é de {a}m²')


print('Calculo de Terreno')
print('-='*25)
l = float(input('Digite a Largura (m): '))
c = float(input('Digite o Comprimento (m): '))
area(l, c)