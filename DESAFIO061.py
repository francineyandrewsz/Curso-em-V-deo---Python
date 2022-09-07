''' Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('=>'*15, 'DESAFIO 061', '<='*15)
print('Gerador de PA')
print('-='*15)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
while cont <= 10:
    print(f' {termo} -> ', end='')
    termo += r
    cont += 1
print('FIM')
