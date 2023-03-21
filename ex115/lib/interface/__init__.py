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


def linha(tam=42):
    return '\033[1;33m-\033[m' * 42


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[1;36mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[1;35m{c}\033[m - \033[1;34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaint('\033[1;36mSua Opção\033[m: ')
    return opc