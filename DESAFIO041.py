'''A Confederação Nacional de Natação precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

print('=>'*20, 'DESAFIO 041', '<='*20)

from datetime import date

nasc = int(input('Ano de nascimento: '))

#Ano atual
ano_atual = date.today().year

idade = ano_atual - nasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
