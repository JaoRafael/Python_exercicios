frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]#modo python
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra] #MODO TRADICIONAL'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um Palindromo!')
else:
 print('A frase \033[31mNÃO\033[m é um palindormo')