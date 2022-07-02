'''Escreva um programa que pergunte a quantidade de km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule 
o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
'''

print('=>'*20, 'DESAFIO 015', '<='*20)

#informe os dias alugados do carro
dias = int(input('Quantos dias alugados? '))

#informe os km percorridos do carro
km = float(input('Quantos Km rodados? '))

#calcule o preço
preço = dias * 60 + km * 0.15

#imprimir o total do pagamento
print(f'O total a pagar é de R${preço:.2f}')
