'''Crie um programa que leia um número inteiro e mostre na tela
se ele é PAR ou ÍMPAR.'''

print('=>'*20, 'DESAFIO 030', '<='*20)

#O usuário deve digitar um número
n = int(input('Me diga um número qualquer: '))

#Se o resultado for igual a zero, o número é PAR
if n % 2 == 0:
    print(f'O número {n} é PAR.')
else:
    print(f'O número {n} é ÍMPAR.')
