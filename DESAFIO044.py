'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print('=>'*15, 'DESAFIO 044', '<='*15)
print('='*10, ' LOJA DE ROUPAS ', '='*10)

preço = float(input('Preço das compras: R$'))
menu = int(input('''FORMAS DE PAGAMENTO
                 [1] à vista dinheiro/cheque
                 [2] à vista cartão
                 [3] 2x no cartão
                 [4] 3x ou mais no cartão
                 Qual é a opção? '''))

if menu == 1:
    desconto = preço - (preço * 10 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${desconto:.2f} no final.')
elif menu == 2:
    desconto = preço - (preço * 5 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${desconto} no final')
elif menu == 3:
    print(f'Sua compra de R${preço:.2f} vai custar R${preço / 2:.2f} em  2x no cartão SEM JUROS.')
elif menu == 4:
    parcel = int(input('Quantas parcelas? '))
    juros = preço + (preço * 20 / 100)
    print(f'Sua compra de R${preço:.2f} vai custar R${juros / parcel:.2f} em {parcel}x no cartão COM JUROS')
else:
    print('ERROR! Você não digitou um valor válido!')
    