print('====== DESAFIO 37 ======')
limpo = '\33[m'
vermelho = '\33[1;91m'
verde = '\33[1;92m'
azul = '\33[1;34m'
amarelo = '\33[1;33m'
roxo = '\33[1;35m'

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

# O python já tem esses conversores dentro dele: binário(bin), OCTAL(oct) e HEXA(hex)
if opcao == 1:
    print(f'{azul}{num}{limpo} convertido para {roxo}BINÁRIO{limpo} é igual a: '
          f'{verde}{bin(num) [2:]}{limpo}')
elif opcao == 2:
    print(f'{azul}{num}{limpo} convertido para {vermelho}OCTAL{limpo} é igual a: '
          f'{verde}{oct(num) [2:]}{limpo}')
elif opcao == 3:
    print(f'{azul}{num}{limpo} convertido para {amarelo}HEXADECIMAL{limpo} é igual a: '
          f'{verde}{hex(num) [2:]}{limpo}')
else:
    print('Opção inválida, digite apenas números de 1 a 3!')
