'''Crie um programa que leia o nome de uma cidade diga se ela começa 
ou não com o nome "SANTO".'''

print('=>'*20, 'DESAFIO 024', '<='*20)

#O usuário deve digitar o nome da cidade
city = str(input('Em que cidade você nasceu? ')).strip().upper()

#imprimir o nome da cidade
print(city[:5] == 'SANTO')

