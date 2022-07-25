'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
print('=>'*20, 'DESAFIO 040', '<='*20)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

média = (nota1 + nota2) / 2

print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno fica {média:.1f}')

if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
else:
    print('O aluno está APROVADO.')
