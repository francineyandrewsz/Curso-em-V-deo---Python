'''Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteie() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores PARES  sorteados pela função anterior.'''
print('=>'*15, 'DESAFIO 100', '<='*15)
from random import *
from time import sleep

def sorteie(lista):
    print('Somando os valores da lista: ', end='')
    for c in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
    

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
    
números = list()
sorteie(números)
somaPar(números)
