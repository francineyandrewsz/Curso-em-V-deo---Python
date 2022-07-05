'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

Ex: Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.
'''

print('=>'*20, 'DESAFIO016', '<='*20)

#o usuário precisa digitar um número
n = float(input('Digite um número: '))

#o programa vai imprimir o número digitado e a sua parte inteira.
print(f'O número {n} tem a parte Inteira {int(n)}')

