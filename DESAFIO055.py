'''Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''
print('=>'*15, 'DESAFIO 055', '<='*15)
maior = 0
menor = 0
for q in range(1, 6):
    p = float(input(f'Peso da {q}ª pessoa: '))
    if q == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
