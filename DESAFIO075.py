'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
print('=>'*15, 'DESAFIO 075', '<='*15)
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um números: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 aparece {núm.count(9)} vez(es)')
if 3 in núm:
    print(f'O valor 3 está na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('Os números pares foram: ', end='')
for n in núm:
    if n % 2 == 0:
        print(f'{n}', end=' ')
