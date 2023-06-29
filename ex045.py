from time import sleep
from random import randint

print('====== DESAFIO 45 ======')

print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogada = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-' * 10)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[jogada]}')
print('-=-' * 10)

if jogada == pc:
    print('EMPATE!!!')
elif jogada == 0 and pc == 2 or jogada == 1 and pc == 0 or jogada == 2 and pc == 1:
    print('JOGADOR VENCEU!!!')
else:
    print('JOGADOR PERDEU!!!')
