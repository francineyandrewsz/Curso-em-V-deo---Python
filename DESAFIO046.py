'''Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, 
com uma pausa de 1 segundo entre eles.'''

print('=>'*15, 'DESAFIO 046', '<='*15)

from time import sleep

for cont in range(10, -1, -1):#Fazer a contagem de 10 até 0 usando -1
    print(cont)#Imprimir a contagem de 10 até 0
    sleep(1)

print('BUM! BUM! POOOW!')
