print('====== DESAFIO 31 ======')
limpo = '\33[m'
AzulClaro = '\33[1;94m'

viagem = float(input('Qual é a distancia da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {AzulClaro}{viagem:.1f}Km.{limpo}')

if viagem <= 200:
    valor = viagem * 0.5
else:
    valor = viagem * 0.45
#valor = distancia * 0.5 if viagem <= 200 else viagem * 0.45

print(f'E o preço da sua passagem será de {AzulClaro}R${valor:.2f}{limpo}')
