'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

print('=>'*15, 'DESAFIO 060', '<='*15)
n = int(input('Digite um número para\ncalcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else' = ', end='')
    f *= c
    c -= 1
print(f)
