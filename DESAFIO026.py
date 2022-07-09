''' Faça um programa que leia uma frase pelo teclado e mostre quantas vezes 
 aparece a letra "A", em que posição ela aparece a primeira vez e em que posição
 ela aparece a última vez.'''

print('=>'*20, 'DESAFIO 026', '<='*20)

#O usuário precisa digitar uma frase
frase = str(input('Digite uma frase: ')).strip().upper()

#imprimir a quantidade de letras A encontradas na frase
print(f'A letra A aparece {frase.count("A")} vezes na frase')
#imprimir a posição da primeira letra A na frase
print(f'A primeira letra A aparece na posição {frase.find("A")+1}')
#imprimir a posição da última letra A na frase
print(f'A última letra A aparece na posição {frase.rfind("A")+1}')
