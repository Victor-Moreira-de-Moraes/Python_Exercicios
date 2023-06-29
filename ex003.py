print('====== DESAFIO 03 ======')
limpo = '\33[m'
AzulClaro = '\33[1;36m'
azul = '\33[1;34m'
vermelho = '\33[1;31m'

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print(f'A soma entre {AzulClaro}{n1}{limpo} e {azul}{n2}{limpo} é {vermelho}{s}{limpo}!')

