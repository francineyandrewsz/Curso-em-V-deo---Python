'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
print('=>'*15, 'DESAFIO 059', '<='*15)
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    opção = int(input('''[1] somar
                      [2] multiplicar
                      [3] maior
                      [4] novos números
                      [5] sair do programa
                      Qual é a sua opção?\n'''))
    if opção == 1:
        print(f'A soma de {n1} + {n2} é {n1+n2}')
    elif opção == 2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        else:
            maior = n1
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        break
    else:
        print('Opção inválida!')
    sleep(2)

print('Fim do Programa!')
        
    