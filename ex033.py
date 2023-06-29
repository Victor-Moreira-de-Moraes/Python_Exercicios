print('====== DESAFIO 33 ======')
limpo = '\33[m'
amarelo = '\33[1;93m'

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Verificando quem é menor
'''
if a < b and a < c:
    menor = a
'''
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor digitado foi {amarelo}{menor}{limpo}')
print(f'O maior valor digitado foi {amarelo}{maior}{limpo}')
