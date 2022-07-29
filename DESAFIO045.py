#Crie um programa que faça o computador jogar Jokenpô com você.

print('=>'*15, 'DESAFIO 045', '<='*15)

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('''Suas opções:
                    [0] PEDRA
                    [1] PAPEL
                    [2] TESOURA
                    Qual é a sua jogada? '''))

computador = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-=-'*10)
print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogador]}')
print('-=-'*10)

if computador == 0:#Computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('ERROR! JOGADA INVÁLIDA!')
elif computador == 1:#Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('ERROR! JOGADA INVÁLIDA!')
elif computador == 2:#Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('ERROR! JOGADA INVÁLIDA!')
    
    