peso = float(input('Digite o seu Peso: (Kg) '))
altura = float(input('Digite a sua altuta: (M) '))
imc = peso / (altura ** 2)
print(f'O  seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você esta Abaixo do peso!')
elif 18.5 <= imc <= 25:
    print('Você esta no peso Ideal!')
elif 25 <= imc <= 30:
    print('Voê esta com Sobrepeso!')
elif 30 <= imc <= 40:
    print('Você está com Obesidade!')
else:
    print('Voce está com \033[1;31mObesidade Morbida\033[m !!!')
    
