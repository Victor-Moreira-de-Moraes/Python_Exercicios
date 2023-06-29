limpo = '\33[m'
vermelho = '\33[1;31m'
ciano = '\33[1;36m'
verde = '\33[1;92m'
amarelo = '\33[1;33m'
azul = '\33[1;34m'
roxo = '\33[1;35m'

print('========== DESAFIO 44 ===============')
print(f'{azul}========== LOJAS GUANABARA =========={limpo}')

compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pagamento = int(input('Qual é a opção? '))

if pagamento == 1:
    desconto = compras - compras * 0.1
    print(f'Sua compra de R${compras:.2f} vai custar {ciano}R${desconto:.2f}{limpo} no final.')

elif pagamento == 2:
    desconto = compras - compras * 0.05
    print(f'Sua compra de R${compras:.2f} vai custar {ciano}R${desconto:.2f}{limpo} no final.')

elif pagamento == 3:
    parcelamento = compras / 2
    print(f'Sua compra de {compras:.2f} será parcelada em 2x de '
          f'{ciano}R${parcelamento:.2f}{limpo} {verde}SEM JUROS{limpo}.')

elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = compras * 0.2 + compras
    parcelamento = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de '
          f'{ciano}R${parcelamento:.2f}{limpo} {amarelo}COM JUROS{limpo}.')
    print(f'Sua compra de R${compras:.2f} vai custar {ciano}R${total:.2f}{limpo} no final.')

else:
    print(f'{vermelho}OPÇÃO INVÁLIDA{limpo} de pagamento, tente novamente!!!')
