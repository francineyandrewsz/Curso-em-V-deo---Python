'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.'''
print('=>'*15, 'DESAFIO 054', '<='*15)
from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    p = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    i = ano_atual - p
    if i >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoa(s) maior(es) de idade')
print(f'E também tivemos {menor} pessoa(s) menor(es) de idade')
