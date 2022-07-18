#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

print('=>'*20, 'DESAFIO 032', '<='*20)

from calendar import isleap
from datetime import date

ano = int(input('Que ano quer analisar?\nColoque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if isleap(ano):
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')
    