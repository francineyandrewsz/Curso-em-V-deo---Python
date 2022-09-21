'''Faça um programa que leia 5 valores numéricos e 
guarde-os em uma lista. No final, mostre qual foi o 
maior e o menor valor digitado e as suas respectivas
posições na lista. '''
print('=>'*15, 'DESAFIO 078', '<='*15)
lista_núm = []
maior = menor = 0 
while True:
    try:
        for c in range(0, 5):
            lista_núm.append(int(input(f'Digite um valor para a Posição {c}: ')))
            if c == 0:
                maior = menor = lista_núm[c]
            else:
                if lista_núm[c] > maior:
                    maior = lista_núm[c]
                if lista_núm[c] < menor:
                    menor = lista_núm[c]
        break
    except:
        print('Operação inválida! Tente novamente...')
print(f'Você digitou os Valores {lista_núm}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista_núm):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista_núm):
    if v == menor:
        print(f'{i}...', end='')
print()
    