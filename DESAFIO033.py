#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('=>'*20, 'DESAFIO 033', '<='*20)

#Leia três valores
v1 = int(input('Primeiro Valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

numbers = [v1, v2, v3]

#Imprimir o maior e menor deles
print(f'O maior valor digitado foi {max(numbers)}')
print(f'O menor valor digitado foi {min(numbers)}')

