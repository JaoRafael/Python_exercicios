dist = float(input('Qual a distância da Viagem? '))
print(f'Você está prestes a começar uma Viagem de {dist}km. ')
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f'E o preço da sua ássagem será R${preco:.2f} ')