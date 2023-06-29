print('====== DESAFIO 34 ======')
limpo = '\33[m'
azul = '\33[1;94m'
verde = '\33[1;92m'

salario = float(input(f'Qual é o salário do funcionário? R$ '))

if salario <= 1250:
    aumento = salario * 0.15 + salario
else:
    aumento = salario * 0.1 + salario
print(f'Quem ganhava {azul}R${salario:.2f}{limpo} passa a ganhar {verde}R${aumento:.2f}{limpo} agora.')
