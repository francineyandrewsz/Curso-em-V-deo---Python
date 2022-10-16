'''Faça um programa que leia nome e peso de várias pessoas, 
quardando tudo em uma lista. No final, mostre:
A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.
'''
print('=>'*15, 'DESAFIO 084', '<='*15)
def cad_pes():
    pes = list()
    dados = list()
    maior = menor = 0
    while True:
        pes.append(str(input('Nome: ')))
        pes.append(float(input('Peso: ')))
        if len(dados) == 0:
            maior = menor = pes[1]
        else:
            if pes[1] > maior:
                maior = pes[1]
            if pes[1] < menor:
                menor = pes[1]     
        dados.append(pes[:])
        pes.clear()
        resp = str(input('Quer continuar? [S/N]\n')).upper()[0]
        if resp == 'S':
            continue
        elif resp == 'N':
            break
        else:
            print('Error!')       
    print('-='*30)
    print(f'Ao todo você cadastrou {len(dados)} pessoas')
    print(f'O maior peso foi {maior} Kg. Peso de ', end='')
    for p in dados:
        if p[1] == maior:
            print(f'[{p[0]}]', end='')
    print()
    print(f'O menor peso foi {menor} Kg. Peso de ', end='')
    for p in dados:
        if p[1] == menor:
            print(f'[{p[0]}]', end='')
    print()   
cad_pes()
