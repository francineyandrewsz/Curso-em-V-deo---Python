'''Crie um programa onde o usuário possa digitar cinco valores númericos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final mostre a lista ordenada na tela.'''
print('=>'*15, 'DESAFIO 080', '<='*15)
valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1        
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')
