'''Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os 
valores únicos digitados, em ordem crescente. '''
print('=>'*15, 'DESAFIO 079', '<='*15)
números = list()
while True:
    try:
        n = int(input('Digite um valor: '))
        if n not in números:
            números.append(n)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado! Não vou adicionar...')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'S':
            continue
        elif resp == 'N':
            break
    except:
        print('Operação inválida! Tente novamente...')
print('-='*30)
print(f'Você digitou os valores {sorted(números)}')
