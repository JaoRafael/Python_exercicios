a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c
print(f'O Menor valor digitado foi {menor}')
print(f'O Maior valor digitado foi {maior}')
