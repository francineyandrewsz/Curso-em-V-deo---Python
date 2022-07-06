'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

print('=>'*20, 'DESAFIO 019', '<='*20)

#Importar choice daa biblioteca random
from random import choice

#O usuário digita o nome dos alunos
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

#fazer uma lista dos alunos
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

#através da biblioteca random o programa vai escolher o aluno dentro da variável lista_alunos
escolhido = choice(lista_alunos)

#imprimir o resultado
print(f'O aluno escolhido foi {escolhido}')
