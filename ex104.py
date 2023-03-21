def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO!\033[m\033[31m Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número \033[1;34m{n}\033[m')