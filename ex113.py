def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Por favor digite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


num = leiaint('Digite um valor inteiro: ')
flo = leiafloat(('Digite um valor real: '))
print(f'O valor digitado foi \033[1;32m{num}\033[m e o real foi \033[1;32m{flo}\033[m')