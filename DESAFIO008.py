'''Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.'''

print('=>'*20, 'DESAFIO 008', '<='*20)
valor = float(input('Uma distância em metros: '))
km = valor/1000
hm = valor/100
dam = valor/10
dm = valor*10
cm = valor*100
mm = valor*1000
print(f'A medida de {valor}m corresponde a\n{km}km)\n{hm}hm\n{dam}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm')
