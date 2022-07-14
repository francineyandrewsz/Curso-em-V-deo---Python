'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem 
dizendo que ele foi multado. A multa vai custar 
R$7,00 por cada Km acima do limite.'''

print('=>'*20, 'DESAFIO 029', '<='*20)

#O usuário deve digitar o km de velocidade do carro
velo = float(input('Qual a velocidade atual do carro? '))

#Condição se a velocidade ficou acima de 80 km
if velo > 80:
    #Imprima o resultado da multa
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    multa = (velo - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')

#Imprima o resultado sem a multa
print('Tenha um bom dia! Dirija com segurança!')
