'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados em um dicionário e todos os dicionários em uma
lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
'''
print('=>'*15, 'DESAFIO 094', '<='*15)
dados = dict()
pessoas = list()
soma = média = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERROR! Digite M ou F. ')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]\n')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Digite S ou F. ')
    if resp == 'N':
        break     
média = soma / len(pessoas)
print('-='*30)   
print(pessoas)
# A)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
# B)
print(f'A média de idade do grupo de pessoas é de {média:5.2f} anos.')
# C)
print(f'As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
# D)
print('Lista das pessoas que estão acima da média.')
for p in pessoas:
    if p['idade'] >= média:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')

