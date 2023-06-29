from math import hypot

print('====== DESAFIO 17 ======')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')
# ou
hipo = (co**2 + ca**2) ** (1/2)
print(f'A hipotenusa vai medir {hipo:.2f}')

