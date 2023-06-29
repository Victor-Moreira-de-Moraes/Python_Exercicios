from math import trunc

print('====== DESAFIO 16 ======')

num = float(input('Digite um número: '))

print(f'O número {num} tem a parte inteira {trunc(num)}.')
# ou
print(f'O número {num} tem a parte inteira {int(num)}.')