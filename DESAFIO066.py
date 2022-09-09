'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

print('=>'*15, 'DESAFIO 066', '<='*15)
soma = quant = 0
while True:
    try:
        valor = int(input('Digite um valor (999 para parar):\n'))
        if valor == 999:
            break
        soma += valor
        quant += 1
    except:
        print('Opção inválida! Tente novamente.')
print(f'A soma dos {quant} valor(es) foi {soma}.')
       