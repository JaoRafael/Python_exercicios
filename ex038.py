n1 = int(input('Digete o \033[;33mPrimeiro\033[m Número inteiro: '))
n2 = int(input('Digite o \033[;34mSegundo\033[m número inteiro: '))
if n1 > n2:
    print('o \033[;33mPRIMEIRO\033[m Número é maior!')
elif n1 < n2:
    print('O \033[;34mSEGUNDO\033[m Número é maior!')
else:
    print('Os \033[31mNÚMEROS\033[m são iguais!!')