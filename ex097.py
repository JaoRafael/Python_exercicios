from time import sleep


def escreva(msg):
    tam = len(msg) + 4
    print('\033[32m=\033[m' * tam)
    print(f'  {msg}')
    print('\033[32m=\033[m' * tam)
    sleep(1)


escreva('João Rafael Guazelli')
escreva('Sa.')
escreva('A merendeira desce, o onibus sai, Dona maria já se foi...')