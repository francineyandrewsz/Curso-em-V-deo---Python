'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
print('=>'*15, 'DESAFIO 051', '<='*15)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
déc = t1 + (10 - 1) * r
for c in range(t1, déc+r, r):
    print(f' {c} ', end='=> ')
print('ACABOU!')
