'''Faça um programa que leia o nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre
o conteúdo da estrutura na tela.'''
print(f'=>'*15, 'DESAFIO 090', '<='*15)
aluno = {'Nome':str, 'Média':float, 'Situação':str}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Média'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
    