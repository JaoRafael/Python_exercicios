from time import sleep
c = ('\033[0m',     #sem cor
     '\033[1;31m',  #vermelho
     '\033[1;32m',  #verde
     '\033[1;33m',  #amarelo
     '\033[1;34m',  #azul
     '\033[1;35m',  #roxo
     '\033[1;36m',  #ciano
     '\033[1;37m',  #cinza
     '\033[30m')    #preto


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[7], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)
    print(c[3], end='')
    sleep(0.5)


comando = ''
while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    sleep(0.5)
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    sleep(0.5)
titulo('  Até a Próxima', 1)
