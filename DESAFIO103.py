'''Faça um programa que tenha uma função chamada ficha(), que receba
dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha informado corretamente.'''
print('=>'*15, 'DESAFIO 103', '<='*15)

def ficha(jogador='<desconhecido>', gols=0):
    print('-'*20)
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato')


# Programa principal
nome = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)    
    