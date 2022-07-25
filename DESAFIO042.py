''' Refaça o DESAFIO 035 dos triângulos, acrescentando o 
recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
print('=>'*20, 'DESAFIO 042', '<='*20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
#Testando se é triângulo
if a < b + c and b < c + a and a < c + b:
    print('Os Segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO!')#Todos os lados iguais
    elif a != b != c != a:
        print('ESCALENO!')#Todos os lados diferentes
    else:
        print('ISÓSCELES!')#Dois lados iguais, um diferente
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo')

    