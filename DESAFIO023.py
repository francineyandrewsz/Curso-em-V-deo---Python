'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada 
um dos dígitos separados.'''

print('=>'*20, 'DESAFIO 023', '<='*20)

#O usuário deve digitar um número de 0 a 9999
núm = int(input('Informe um número: '))
print(f'Analisando o número {núm}')
#O programa faz o cálculo de conversão
u = núm // 1 % 10
d = núm // 10 % 10
c = núm // 100 % 10
m = núm // 1000 % 10

#imprimir os números convertidos
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')


