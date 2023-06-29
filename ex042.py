limpo = '\33[m'
vermelho = '\33[1;31m'
ciano = '\33[1;36m'
verde = '\33[1;92m'
amarelo = '\33[1;33m'
azul = '\33[1;34m'
roxo = '\33[1;35m'

print('====== DESAFIO 42 ======')

a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento: '))
c = float(input('Terceiro Segmento: '))

if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos acima {verde}PODEM{limpo} formar um triângulo ', end='')
    if a == b == c:
        print(f'{azul}Equilátero!{limpo}') # Todos os lados iguais
    elif a != b != c != a:
        print(f'{amarelo}Escaleno!{limpo}') # Todos os lados diferentes
    else:
        print(f'{roxo}Isósceles!{limpo}') # Dois dos lados iguais e um diferente
else:
    print(f'Os segmentos acima {vermelho}NÃO PODEM{limpo} formar um triângulo!')
