''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

print('=>'*20, 'DESAFIO017', '<='*20)

#importe a biblioteca math
import math

#informe o comprimento do cateto oposto
co = float(input('Comprimento do cateto oposto: '))
#informe o comprimento do cateto adjacente
ca = float(input('Comprimento do cateto adjacente: '))

#cálculo através da biblioteca math
h = math.hypot(co, ca)

#imprimir o valor da resultado
print(f'A hipotenusa vai medir {h:.2f}')
