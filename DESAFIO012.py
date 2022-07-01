'''Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
'''


print('=>'*20, 'DESAFIO 012', '<='*20)
preço = float(input('Qual é o preço do produto? R$'))
novo_pr = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço:.2f}, na promoção de 5% vai custar R${novo_pr:.2f}')
