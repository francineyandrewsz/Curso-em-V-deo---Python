'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 parta viagens mais longas.'''

print('=>'*20, 'DESAFIO 031', '<='*20)

#Insira a distância do sua viagem
distância = float(input('Qual é a distância da sua viagem? '))
#Imprima o resultado da viagem em km
print(f'Você está prestes a começar uma viagem de {distância:.1f}Km.')

#Calcule o preço da passagem
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45

#Imprima o preço
print(f'E o preço da sua passagem será de R${preço:.2f}')
     