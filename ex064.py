num = cont = soma = 0
num = int(input('Digite um número [Para parar digite 999]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [Para parar digite 999]: '))
print(f'Você digitou {cont} números e a soma entre eles é de {soma}.')
