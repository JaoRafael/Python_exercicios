print('\033[35m-=\033[m'*20) #segunda parte do ex035
print('Analisador de Triângulo (parte2)')
print('\033[35m-=\033[m'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo! ', end='')
    if r1 == r2 == r3:
        print('\033[30mEQUILÁTERO\033[m !')
    elif r1 != r2 != r3 != r1:
        print('\033[31mESCALENO\033[m !')
    else:
        print('\033[34mISÓSCELES\033[m')
else:
    print('Os segmentos acima NÃO podem formar um Triângulo!')