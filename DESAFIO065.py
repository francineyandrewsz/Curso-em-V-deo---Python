'''Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa deve perguntar ao 
usuário se ele quer ou não continuar a digitar valores.'''

print('=>'*15, 'DESAFIO 065', '<='*15)
res = 'S' 
soma = quant = média = maior = menor = 0
while res in 'S':
    try:
        núm = int(input('Digite um número: '))
        soma += núm
        quant += 1
        if quant == 1:
            maior = menor = núm
        else:
            if núm > maior:
                maior = núm
            if núm < menor:
                menor = núm
        res = str(input('Quer continuar? [S/N]\n')).upper().strip()[0]   
    except:
        print('Opção inválida! Tente novamente.')
média = soma / quant
print(f'Você digitou {quant} número(s) e a média foi {média:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
