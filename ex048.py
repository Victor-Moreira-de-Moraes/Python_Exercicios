print('====== DESAFIO 48 ======')

# Um acumulador soma um valor
soma = 0
# Um contador soma +1
cont = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1 #cont = cont + 1
        soma += n #soma = soma + n
print(f'A soma de todos os {cont} valores solicitados é {soma}')
