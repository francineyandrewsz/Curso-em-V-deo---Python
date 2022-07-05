'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
do seno, cosseno e tangente desse ângulo.'''

print('=>'*20, 'DESAFIO 018', '<='*20)

#importe a biblioteca math
import math

#O usuário digita o ângulo que deseja
ângulo = float(input('Digite o ângulo que você deseja: '))

#O programa faz o cálculo do seno através da biblioteca math
seno = math.sin(math.radians(ângulo))

#imprimir o resultado do seno
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')

#O programa faz o cálculo do cosseno através da biblioteca math
cosseno = math.cos(math.radians(ângulo))

#imprimir o resultado do cosseno
print(f'O ângulo de {ângulo} tem o COSSENO {cosseno:.2f}')

#O programa faz o cálculo da tangente através da biblioteca math
tangente = math.tan(math.radians(ângulo))

#imprimir o resultado da tangente
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')
