''' Faça um programa que leia o nome completo de uma pessoa, mostrando em 
seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.
'''

print('=>'*20, 'DESAFIO 027', '<='*20)

#O usuário deve digitar o nome completo
nome = str(input('Digite seu nome completo: ')).strip().upper()

#O programa vai fazer a separação do nome
pos = nome.split()

#imprimir o nome com suas determinadas posições
print(f'Seu nome completo é {nome}\nSeu primeiro nome é {pos[0]}\nE seu último nome é {pos[-1]}')

