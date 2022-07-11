'''Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.'''

print('=>'*20, 'DESAFIO 028', '<='*20)

#importar randint da biblioteca random
from random import randint
#importar sleep da biblioteca time
from time import sleep

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)

#O jogador tenta advinhar um número
jogador = int(input('Em que número eu pensei? '))
#Faz o computador "PENSAR" em número
computador = randint(0, 5)
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
