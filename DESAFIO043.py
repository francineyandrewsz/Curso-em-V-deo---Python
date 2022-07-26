''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

print('=>'*15, 'DESAFIO 043', '<='*15)

peso = float(input('Qual é o peso? (Kg) '))
alt = float(input('Qual é sua altura? (m) '))

#Calcular massa corporal
imc = peso / (alt ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

#Tabela que mostra o status da pessoa de acordo com o imc
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está com PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado')
 