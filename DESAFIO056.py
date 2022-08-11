'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o 
nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
print('=>'*15, 'DESAFIO 056', '<='*15)
soma_i = 0
média_i = 0
maior_i_h = 0
n_velho = ''
t_mulher20 = 0
for p in range(1, 5):
    print(f'------- {p}ª PESSOA -------')
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    soma_i += i
    if p == 1 and s in 'Mm':
        maior_i_h = i
        n_velho = n
    if s in 'Mm' and i > maior_i_h:
        maior_i_h = i
        n_velho = n
    if s in 'Ff' and i < 20:
        t_mulher20 += 1
média_i = soma_i / 4
print(f'A média de idade do grupo é de {média_i} anos')
print(f'O homem mais velho tem {maior_i_h} e se chama {n_velho}')
print(f'Ao todo são {t_mulher20} mulher(es) com menos de 20 anos')
