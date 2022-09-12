'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
print('=>'*15, 'DESAFIO 070', '<='*15)
print('-'*40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-'*40)
total = quant = maisDmil = menor = 0
barato = ''
while True:
    try:
        nome = str(input('Nome do Produto: '))
        preço = int(input('Preço: R$'))
        quant += 1
        total += preço
        if preço > 1000:
            maisDmil += 1
        if quant == 1 or preço < menor:
            menor = preço
            barato = nome
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N]\n')).strip().upper()[0]
        if resp == 'N':
            break
    except:
        print('Error no programa! Tente novamente.')
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {quant} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
