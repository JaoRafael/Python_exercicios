frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase '
      '\nA primeira letra A aparece na posição {} '
      '\nA última letra A aparece na posição {}'
      .format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))