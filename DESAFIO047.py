#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('=>'*15, 'DESAFIO 047', '<='*15)

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')

print('Acabou!')
