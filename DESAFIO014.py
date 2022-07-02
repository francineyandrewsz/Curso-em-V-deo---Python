'''Escreva um programa que converta uma temperatura digitando em graus
Celsius e converta para graus Fahrenheit.'''

print('=>'*20, 'DESAFIO 014', '<='*20)

#informe o valor da temperatura em Celsius
c = float(input('Informe a temperatura em °C: '))

#aplique a fórmula de conversão para fahrenheit
f = c * 1.8 + 32

#imprimir o resultado da temperatura e conversão
print(f'A temperatura de {c:.1f}°C corresponde a {f:.1f}°F')

