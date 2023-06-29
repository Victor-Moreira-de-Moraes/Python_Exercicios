print('====== DESAFIO 02 ======')
limpo = '\33[m'
verde = '\33[1;32m'

nome = input('Digite seu nome: ')
print('É um prazer em te conhecer,', nome, '!')
print('ou')
print('É um prazer  em te conhecer {}!'.format(nome))
print('ou')
print(f'É um prazer te conhecer {verde} {nome} {limpo}!')