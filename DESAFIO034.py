'''Escreva um programa que pergunte o salário de um funcionário e 
calcule o valor do seu aumento. Para salários superiores a R$1250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

print('=>' * 20, 'DESAFIO 034', '<=' * 20)

salário = float(input('Qual é o salário do funcionário? R$'))

#Condição se o salário é superior, inferior ou igual a R$ 1250,00
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)

print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f}')
