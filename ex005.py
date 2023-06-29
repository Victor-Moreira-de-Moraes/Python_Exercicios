print('====== DESAFIO 05 ======')
limpo = '\33[m'
AmareloClaro = '\33[1;93m'
vermelho = '\33[1;92m'

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print(f'Analisando o valor {AmareloClaro}{n}{limpo}, seu antecessor é {vermelho}{a}{limpo} e seu sucessor é {vermelho}{s}{limpo}!')
# ou
print(f'Analizando o valor {AmareloClaro}{n}{limpo}, seu antecessor é {vermelho}{n-1}{limpo} e seu sucessor é {vermelho}{n+1}{limpo}!')
