from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os numeros sorteados foram: {num} '
      f'\nO maior valor sorteado foi {max(num)} '
      f'\nO menor valor dorteado foi {min(num)}')