import random
# form random import shuffle

print('====== DESAFIO 20 ======')

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)
# shuffle(lista)

print('A ordem de apresentação será')
print(lista)
