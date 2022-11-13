'''Faça um programa que tenha uma função chamada área(), que receba 
as dimensões de um terreno retangular (largura e comprimento) e 
mostre a área do terreno.'''

print('=>'*15, 'DESAFIO 096', '<='*15)

def área(l, c):
    print('  Controle de Terrenos  ')
    print('-'*15)
    print(f'A área de um terreno {l}x{c} é de {l*c}m².')


# Programa principal
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)
