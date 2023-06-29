import random
#from random import choice

print('====== DESAFIO 19 ======')

pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
qua = input('Quarto aluno: ')

lista = [pri, seg, ter, qua]
escolhido = random.choice(lista)
# Uma lista sempre fica entre colchetes

print(f'O aluno escolhido foi {escolhido}.')
