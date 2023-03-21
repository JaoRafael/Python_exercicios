num = int(input('\033[1mDigite um número:\033[m '))
print('''Escolha uma das bases númericas para conversão:
\033[;31m[ 1 ] Converter para BINÁRIO\033[m
\033[;36m[ 2 ] Converter para OCTAL\033[m
\033[;35m[ 3 ] Converter para HEXADECIMAL\033[m''')
opcao = int(input('\033[1mDigite sua opção:\033[m '))
if opcao == 1:
    print(f'\033[;33m{num}\033[m Convertido para \033[;31mBINÁRIO\033[m é igual a \033[;32m{bin(num)[2:]}\033[m')
elif opcao == 2:
    print(f'\033[;33m{num}\033[m Convertido para \033[;36mOCTAL\033[m é igual a \033[;32m{oct(num)[2:]}\033[m')
elif opcao == 3:
    print(f'\033[;33m{num}\033[m Convertido para \033[35mHEXADECIMAL\033[m é igual a \033[32m{hex(num)[2]}\033[m')
else:
    print('Opção INVÁLIDA tente novamente!!')
