'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

print('=>'*20, 'DESAFIO 022', '<='*20)

#O programa pedi para o usuário digitar um nome completo
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

#imprimir o nome todo em maiúsculo
print(f'Seu nome em maiúsculo fica {nome.upper()}')
#imprimir o nome todo em minúsculo
print(f'Seu nome em minúsculo fica {nome.lower()}')
#imprimir a quantidade de letras que tem o nome
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")

#fazer o programa separar o nome
separa = nome.split()

#imprimir somente o primeiro nome e a sua quantidade de letras
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')


