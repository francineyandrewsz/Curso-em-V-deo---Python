'''Crie um programa que vai ler vários números e cololocar em uma lista.
Depois disso , crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, repectivamente. Ao final, mostre
o conteúdo das três geradas.'''
print('=>'*15, 'DESAFIO 082', '<='*15)
valores = []
lista_par = []
lista_ímpar = []
while True:
    try:
        valores.append(int(input('Digite um número: ')))
        resp = str(input('Quer continuar? [S/N]\n')).upper()[0]
        if resp == 'S':
            continue
        elif resp == 'N':
            break
        else:
            print('Error!')
    except:
        print('Operação inválida! Tente novamente...')
print('-='*30)
print(f'A lista completa é {valores}')
for valor in valores:
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_ímpar.append(valor)
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_ímpar}')
