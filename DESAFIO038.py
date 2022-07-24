'''Escreva um programa que leia dois números inteiros e compare-os.
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

print('=>'*20, 'DESAFIO 038', '<='*20)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:#Se o número n1 for maior imprima
    print('O PRIMEIRO valor é maior.')
elif n1 < n2:#Se o número n2 for maior imprima
    print('O SEGUNDO valor é maior')
else:#O número n1 for igual a n2 imprima
    print('Não existe valor maior, os dois são iguais')
