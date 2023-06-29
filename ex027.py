print('====== DESAFIO 27 ======')

nome = str(input('Digite seu nome completo: ')).strip().title()
lista = nome.split()

print(f'É um prazer em te conhecer {nome}!!!')
print(f'Seu primeiro nome é {lista [0]}')
print(f'Seu último nome é {lista[len(lista) - 1]}')
