from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que vc deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}. '
      f'\nO ângulo de {angulo} tem o COSSENO de {cosseno:.2f}. '
      f'\nO ângulo de {angulo} tem a TANGENTE de {tangente:.2f}.')

