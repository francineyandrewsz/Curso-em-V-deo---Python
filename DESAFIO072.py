'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.'''

print('=>'*15, 'DESAFIO 072', '<='*15)
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',    'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    try:
        n = int(input('Digite um número entre 0 e 20:\n'))
        if n > 20:
            n = int(input('Por favor, Digite um número entre 0 e 20:\n'))
        print(f'Você digitou o número {extenso[n]}')
        resp = str(input('Você quer continuar? [S/N]:\n')).strip().upper()[0]
        if resp == 'N':
            break
    except:
        print('Opção inválida! Tente novamente.')
print('==== FIM DO PROGRAMA ====')
