#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('=>'*15, 'DESAFIO 052', '<='*15)
n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[m O número {n} foi divisível {t} vezes.')
if t == 2:
    print('É por isso ele É PRIMO!')
else:
    print('É por isso ele NÃO É PRIMO!')
        