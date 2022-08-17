'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

print('=>'*15, 'DESAFIO 058', '<='*15)
from random import randint
pc = randint(0, 10)
acertou = False
palpites = 0
print('Sou seu computador...')
print('''Acabei de pensar eum um número entre 0 e 10.
      Será que você consegue advinhar qual foi?''')
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente mais uma vez.')
   
print(f'Acertou com {palpites} tentativas. Parabéns!')
        