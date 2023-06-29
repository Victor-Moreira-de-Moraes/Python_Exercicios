limpo = '\33[m'
vermelho = '\33[1;91m'
verde = '\33[1;92m'
amarelo = '\33[1;33m'
azul = '\33[1;94m'
print('====== DESAFIO 40 ======')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

print(f'Tirando {azul}{n1}{limpo} e {azul}{n2}{limpo}, a média do aluno é {azul}{m:.1f}{limpo}!')
if m > 7.0:
    print(f'O aluno está {verde}APROVADO{limpo}!!!')
elif m >= 5.0:
    print(f'O aluno está de {amarelo}RECUPERAÇÃO{limpo}!!!')
else:
    print(f'O aluno foi {vermelho}REPROVADO{limpo}!!!')
