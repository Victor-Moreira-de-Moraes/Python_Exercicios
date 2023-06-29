from datetime import date
limpo = '\33[m'
magenta = '\33[1;95m'
VermelhoClaro = '\33[1;91m'
verde = '\33[1;32m'

print('====== DESAFIO 32 ======')

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Pega o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {magenta}{ano}{limpo} {verde}É BISSEXTO{limpo}!')
else:
    print(f'O ano de {magenta}{ano}{limpo} {VermelhoClaro}NÃO É BISSEXTO{limpo}!')
