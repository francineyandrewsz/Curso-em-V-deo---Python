'''Faça um algoritmo que leia o salário de um funcionário e mostre 
seu novo salário, com 15% de aumento.'''

print('=>'*20, 'DESAFIO 013', '<='*20)

salário = float(input('Digite o salário do funcionário: R$'))
novo = salário + (salário * 15 / 100)

print(f'O salário de R${salário:.2f}, com aumento de 15% ficou R${novo:.2f}')
