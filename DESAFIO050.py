'''Desenvolva um programa que leia seis números inteiros 
e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''

print('=>'*15, 'DESAFIO 050', '<='*15)

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o valor {c}: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} número(s) PAR(ES) e a SOMA foi {soma}')
