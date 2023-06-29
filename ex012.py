print('====== DESAFIO 12 ======')

preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)

print(f'O produto que custava R${preco:.2f},'
      f' na promoção com desconto de 5% vai custar R${novo:.2f}')
