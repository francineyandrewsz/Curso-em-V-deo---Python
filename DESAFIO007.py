'''Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.'''

print('=>'*20, 'DESAFIO007', '<='*20)
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é igual a {m:.1f}')


