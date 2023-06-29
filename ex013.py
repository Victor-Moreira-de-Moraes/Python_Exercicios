print('====== DESAFIO 13 ======')

salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)

print(f'Um funcionário que ganhava R${salario:.2f},'
      f' com 15% de aumento, passa a receber R${novo:.2f}')
