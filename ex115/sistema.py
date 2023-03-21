from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq= 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resp = menu(['Ver pessoas Cadastradas', 'Cadastrar Novas pessoas', 'Sair do Sistema'])
    if resp == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerarquivo(arq)
        sleep(0.5)
    elif resp == 2:
        #Opção de cadastrar um nova pessoa
        cabeçalho('\033[35mNOVO CADASTRO\033[m')
        nome = str(input('\033[1;35mNome\033[m: '))
        idade = leiaint('\033[1;35mIdade\033[m: ')
        cadastrar(arq, nome, idade)
        sleep(0.5)
    elif resp == 3:
        cabeçalho('\033[1;33mSaindo do sistema... é noiz!\033[m')
        sleep(1)
        break
    else:
        print('\033[1;31mERRO!! Digite uma opção válida!\033[m')
    sleep(1)
