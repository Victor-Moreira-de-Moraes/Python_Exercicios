print('====== DESAFIO 06 ======')

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print(f'O dobro de {n} vale {d}!')
print(f'O triplo de {n} vale {t}!')
print(f'A raiz quadrada de {n} vale {r:.2f}!')
# ou
print(f'O dobro de {n} vale {n*2}!')
print(f'O triplo de {n} vale {n*3}!')
print(f'A raiz quadrada de {n} vale {pow(n, (1/2)):.2f}!')
