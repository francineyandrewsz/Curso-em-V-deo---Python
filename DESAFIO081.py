'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
print('=>'*15, 'DESAFIO 081', '<='*15)
valores = []
while True:
    try:
        valores.append(int(input('Digite um valor: ')))
        resp = str(input('Quer continuar? [S/N]\n')).upper()[0]
        if resp == 'S':
            continue
        elif resp == 'N':
            break
    except:
        print('Operação inválida! Tente novamente')
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente são {sorted(valores)[::-1]}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista na posição {valores.count(5)}')
else:
    print('O valor 5 não faz parte da lista')
