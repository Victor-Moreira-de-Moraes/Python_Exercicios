print('====== DESAFIO 08 ======')

d = float(input('Uma distância em metros: '))
mm =d*1000
cm =d*100
dm =d*10
dam = d/10
hm = d/100
km = d/1000

print(f'A medida de {d}m corresponde a: ')
print(f' {km}km \n {dm}hm \n {dam:.2}dam \n {d}m \n '
      f'{dm}dm \n {cm:.0f}cm \n {mm:.0f}mm')
