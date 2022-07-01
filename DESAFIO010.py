'''Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos Dólares ela pode comprar.

Considere US$1,00 = R$5,25

'''

print('=>'*20, 'DESAFIO 010', '<='*20)
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.25
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
euro = real / 5.50
print(f'Com R${real:.2f} você pode comprar £${euro:.2f}')

