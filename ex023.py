print('====== DESAFIO 23 ======')

#num = int(input('Informe um número: '))
#n = str(num)

#print(f'Analizando o número {num} temos:')
#print(f'Unidade: {n[3]}')
#print(f'Dezena: {n[2]}')
#print(f'Centena: {n[1]}')
#print(f'Milhar: {n[0]}')

# Em cima foi trabalhado com strings, mas como ainda não podemos
# trabalhar com if e else, vamos utilizar a maneira matemática.

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analizando o número {num} temos:')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
