print('====== DESAFIO 43 ======')

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / altura ** 2

print(f'O IMC dessa pessoa é de {imc:.1f}')
print('Você está ', end='')
if imc >= 40:
    print('com OBESIDADE MÓRBIDA!')
elif imc >= 30:
    print('com OBESIDADE!')
elif imc >= 25:
    print('com SOBREPESO!')
elif imc >= 18.5:
    print('no PESO IDEAL!')
else:
    print('ABAIXO DO PESO!')
