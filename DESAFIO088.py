'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
print('=>'*15, 'DESAFIO 088', '<='*15)
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('    JOGO DA MEGA SENA      ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0 
    while True:
        núm = randint(1, 60)
        if núm not in lista:
            lista.append(núm)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {sorted(l)}')
    sleep(1)
print('-='*3, '<BOA SORTE!>', '-='*3)
