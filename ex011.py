print('====== DESAFIO 11 ======')

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
tinta = area / 2

print(f'Sua parede tem a dimensão de {l} X {a} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta!')
