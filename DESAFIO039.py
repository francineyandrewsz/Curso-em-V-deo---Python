''' Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

print('=>'*20, 'DESAFIO 039', '<='*20)

from datetime import date

nasc = int(input('Ano de nascimento: '))

#ano atual
ano_atual = date.today().year
#Sua idade
idade = ano_atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.')

if idade < 18:
    tempo = 18 - idade
    print(f'Ainda falta {tempo} anos para o alistamento')
    print(f'Seu alistamento será em {ano_atual + tempo}.')
elif idade > 18:
    tempo = idade - 18
    print(f'Você já deveria ter se alistado há {tempo} anos.')
    print(f'Seu alistamento foi em {ano_atual - tempo}.')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
    
