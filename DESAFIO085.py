'''Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
print('=>'*15, 'DESAFIO 085', '<='*15)
núm = [[], []]
valores = 0
for c in range(1, 8):
    valores = int(input(f'Digite o {c}º valor: '))
    if valores % 2 == 0:
        núm[0].append(valores)
    else:
        núm[1].append(valores)
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(núm[0])}')
print(f'Os valores ímpares digitados foram: {sorted(núm[1])}')
