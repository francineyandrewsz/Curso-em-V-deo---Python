'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''
print('=>'*15, 'DESAFIO 069', '<='*15)
mais_De_18 = total_h = mulher_Menos_20 = 0
while True:
    try:
        print('-'*30)
        print('     CADASTRE UMA PESSOA     ')
        print('-'*30)
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            mais_De_18 += 1
        if sexo == 'M':
            total_h += 1
        if sexo == 'F' and idade < 20:
            mulher_Menos_20 += 1
        print('-'*30)
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    except:
        print('Error no programa! Digite um valor válido.')
print(f'Total de pessoas com mais de 18 anos: {mais_De_18}')
print(f'Ao todo temos {total_h} homem(ns) cadastado(s)')
print(f'E temos {mulher_Menos_20} mulher(es) com menos de 20 anos')
