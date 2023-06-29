from random import randint
from time import sleep # Faz o computador esperar um tempo antes de mostrar o próximo comando

print('====== DESAFIO 28 ======')

computador = randint(0, 1) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar
print('PROCESSANDO...')
sleep(2) # sleep(quantos segundos vc quer de espera)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eupensei no número {computador} e não no {jogador}!')
