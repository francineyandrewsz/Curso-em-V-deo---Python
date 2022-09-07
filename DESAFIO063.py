'''Escreva um programa que leia um número N inteiro qualquer e mostre 
na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

'''
print('=>'*15, 'DESAFIO 063', '<='*15)
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar?\n'))
t1 = 0
t2 = 1
cont = 3
print('~'*30)
print(f'{t1} -> {t2}', end='')
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
