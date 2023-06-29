import math
from math import cos, sin, tan, radians

print('====== DESAFIO 18 ======')

ang = float(input('Digite o ângulo que você deseja: '))

# O sin, cos e tan transforma o ângulo escolhido em radianos,
# por isso temos que transforma-lo em graus com o radians

print(f'O ângulo de {ang} tem o SENO de {sin(radians(ang)):.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cos(radians(ang)):.2f}')

tangente = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem a TANGENTE de {tangente:.2f}')
