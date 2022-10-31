'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de
ZERO, o dicionário receberá o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''
print('=>'*15, 'DESAFIO 092', '<='*15)
from datetime import datetime
cad = dict()
cad['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cad['Idade'] = datetime.now().year - nasc
cad['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cad['CTPS'] != 0:
    cad['Contratação'] = int(input('Ano de contratação: '))
    cad['Salário'] = float(input('Salário: R$'))
    cad['Aposentadoria'] = cad['Idade'] + ((cad['Contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in cad.items():
    print(f'  - {k} tem valor {v}')
