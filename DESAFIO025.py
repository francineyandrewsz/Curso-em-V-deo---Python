'''Crie um programa que leia o nome de uma pessoa e diga 
se ela tem "SILVA" no nome.'''

print('=>'*20, 'DESAFIO 025', '<='*20)

nome = str(input('Qual é seu nome completo? ')).strip()

print('Seu nome tem "Silva"? {}'.format('Silva'in nome.lower()))

