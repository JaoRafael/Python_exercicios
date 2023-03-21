resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
'''faz com que todas as letras fiquem maiusculas e pegue apenas a primeira letra'''
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media:.2f} '
      f'\nO maior valor digitado foi {maior} e o menor foi {menor}')