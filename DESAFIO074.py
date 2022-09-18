''' Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla. Depois disso, mostre a listagem de 
números gerados e também indique o menor e o maior valor 
que estão na tupla.'''
print('=>'*15, 'DESAFIO 074', '<='*15)
from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in números:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
