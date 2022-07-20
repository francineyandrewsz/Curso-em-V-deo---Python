'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.'''

print('=>' * 20, 'DESAFIO 035', '<=' * 20)
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

#Condição para formar triângulo
if a < b + c and b < a + c and c + a < b:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
