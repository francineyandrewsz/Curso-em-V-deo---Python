'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('=>'*20, 'DESAFIO 036', '<='*20)

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

#Calcule a prestação da casa
prestação = casa / (anos * 12)

#30% do salário
mínimo = salário * 30 / 100

print(f'Para pegar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestação:.2f}')

#Condição da prestação com relação ao salário
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
    
