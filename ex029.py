print('====== DESAFIO 29 ======')

velocidade = float(input('Qual é a velocidade atual do carro? '))


if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R$ {multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
