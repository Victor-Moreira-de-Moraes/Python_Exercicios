from datetime import date
limpo = '\33[m'
vermelho = '\33[1;91m'
verde = '\33[1;92m'
amarelo = '\33[1;33m'
print('====== DESAFIO 39 ======')

nascimento = int(input('Ano de nascimento: '))
atual = date.today().year # Pega o ano atual
idade = atual - nascimento

print(f'Quem nasceu em {verde}{nascimento}{limpo} tem {amarelo}{idade}{limpo}'
      f' anos em {vermelho}{atual}{limpo}.')
if idade == 18:
    print(f'Você tem que se alistar {vermelho}IMEDIATAMENTE!!!{limpo}')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {amarelo}{saldo}{limpo}'
          f' anos para o alistamento!')
    ano = atual + saldo
    print(f'Seu alistamento será em {amarelo}{ano}{limpo}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {verde}{saldo}{limpo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {verde}{ano}{limpo}.')
