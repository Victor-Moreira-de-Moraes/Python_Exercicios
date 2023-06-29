print('====== DESAFIO 35 ======')
limpo = '\33[m'
vermelho = '\33[1;31m'
ciano = '\33[1;36m'
verde = '\33[1;92m'

print(f'{ciano}-=-{limpo}' * 20)
print(f'{verde}Analisador de Triângulos{limpo}')
print(f'{ciano}-=-{limpo}' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima {ciano}PODEM{limpo} formar triângulo')
else:
    print(f'Os segmentos acima {vermelho}NÃO PODEM{limpo} formar triângulo')
