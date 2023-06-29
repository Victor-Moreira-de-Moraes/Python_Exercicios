print('====== DESAFIO 04 ======')
limpo = '\33[m'
roxo = '\33[1;35m'

a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a))

print(f'Só tem {roxo}espaços{limpo}? ', a.isspace())
print(f'É um {roxo}número{limpo}? ', a.isnumeric())
print(f'É {roxo}alfabético{limpo}? ', a.isalpha())
print(f'É {roxo}alfanumérico{limpo}?', a.isalnum())
print(f'Está em {roxo}maiúsculas{limpo}?', a.isupper())
print(f'Está em {roxo}minuscúlas{limpo}?', a.islower())
print(f'Está {roxo}capitalizada{limpo}?', a.istitle())

# Capitalizada: É quando a palavra começa com uma letra maiúscula e o resto é minúscula.