''' Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

print('=>'*15, 'DESAFIO 057', '<='*15)
s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos! Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {s} registrado com sucesso')
if s == 'M' or s == 'm':
    print('Sexo masculino registrado com sucesso')
elif s == 'F' or s == 'f':
    print('Sexo feminino registrado com sucesso')     
     