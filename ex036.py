print('====== DESAFIO 36 ======')
limpo = '\33[m'
vermelho = '\33[1;91m'
verde = '\33[1;92m'
azul = '\33[1;34m'

casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.3

# Se o empréstimo passar de 30% do salário, empréstimo negado
print(f'Para pagar uma casa de {azul}R${casa:.2f}{limpo} em {azul}{anos}{limpo} anos ', end='')
print(f'a prestação será de {azul}R${prestacao:.2f}{limpo}')
if prestacao <= minimo:
    print(f'Empréstimo {verde}APROVADO!!!{limpo}')
else:
    print(f'Empréstimo {vermelho}NEGADO!!!{limpo}')
