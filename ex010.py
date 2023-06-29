print('====== DESAFIO 10 ======')

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real/3.27
euro = real/5.55
kwanza = real*98.56

print(f'Com R${real} você pode comprar Kz${kwanza:.2f}')
print(f'Com R${real} você pode comprar Є{euro:.2f}')
print(f'Com R${real} você pode comprar US${dolar:.2f}')
#ou print(f'Com R${real} você pode comprar US${real/3.27:.2f}')

