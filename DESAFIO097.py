'''Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre  uma
mensagem com tamanho adaptável.

Ex: escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~~~
  Olá, Mundo!
~~~~~~~~~~~~~~
'''
print('=>'*15, 'DESAFIO 097', '<='*15)
def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f'  {texto}')
    print('~' * tam)


# Programa principal
escreva('Franciney Andrews')
escreva('PYTHON')
escreva('Quero ganhar muito DINHEIROOOOOOOOO!!!')
