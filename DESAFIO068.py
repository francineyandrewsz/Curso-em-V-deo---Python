''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo. '''

print('=>'*15, 'DESAFIO 068', '<='*15)
from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
acertos = 0
while True:
    try:
        jogador = int(input('Digite um número: '))
        computador = randint(0, 10)
        total = jogador + computador
        resp = ' '
        while resp not in 'PI':
            resp = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
        print('-'*40)
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
        print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
        print('-'*40)
        if resp == 'P':
            if total % 2 == 0:
                print('Você VENCEU!')
                acertos += 1
            else:
                print('Você PERDEU!')
                print('-='*15)
                break
        if resp == 'I':
            if total % 2 == 1:
                print('Você VENCEU!')
                acertos += 1
            else:
                print('Você PERDEU!')
                print('-='*15)
                break
        print('Vamos jogar novamente...')
        print('-='*15)                     
    except:
        print('Error no programa! Digite um valor válido.')
print(f'GAME OVER! Você acertou {acertos} vez(es).') 
