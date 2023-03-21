from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>> Qual a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Peimeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, Tente novamente...')
    print('\033[1\-=\033[m'*18)
    sleep(1)
print('Obrigado volte sempre!!')