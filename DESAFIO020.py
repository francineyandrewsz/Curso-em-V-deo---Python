''' O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

print('=>'*20, 'DESAFIO 020', '<='*20)

#importa shuffle da biblioteca random
from random import shuffle

#O usuário deve digitar o nome dos alunos
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

#O programa deve colocar o nome digitado dos alunos em uma lista
lista_alunos = [aluno1, aluno2, aluno3, aluno4]

#o programa vai selecionar a ordem de cada item da lista
shuffle(lista_alunos)

#imprimir a ordem da lista
print(f'A ordem de apresentação será\n{lista_alunos}')
