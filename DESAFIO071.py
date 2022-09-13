''' Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('=>'*15, 'DESAFIO 071', '<='*15)
print('='*40)
print('{:^40}'.format('BANCO ANDREWS'))
print('='*40)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cédulas = 50
tot_céd = 0
while True:
    if total >= cédulas:
        total -= cédulas
        tot_céd += 1
    else:
        if tot_céd > 0:
            print(f'Total de {tot_céd} cédulas de R${cédulas}')
        if cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 1
        tot_céd = 0
        if total == 0:
            break
print('='*40)
print('Volte sempre ao BANCO ANDREWS! Tenha um Bom dia')
