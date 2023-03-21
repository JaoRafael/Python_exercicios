num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer contnuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'\033[1m-=\033[m'*30)
print(f'A Lista completa é {num}'
      f'\nA lista de pares é {par}'
      f'\nA lista de impares é {impar}')
