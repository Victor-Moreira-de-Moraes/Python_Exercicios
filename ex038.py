print('====== DESAFIO 38 ======')
limpo = '\33[m'
vermelho = '\33[1;91m'
verde = '\33[1;92m'
amarelo = '\33[1;33m'

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

if a > b:
    print(f'O {verde}PRIMEIRO{limpo} valor é maior!')
elif b > a:
    print(f'O {amarelo}SEGUNDO{limpo} valor é maior!')
else:
    print(f'Os dois são {vermelho}IGUAIS{limpo}!')
