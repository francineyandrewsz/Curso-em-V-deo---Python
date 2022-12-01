'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será um 
valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.'''
print('=>'*15, 'DEASFIO 102', '<='*15)
def fatorial(núm, show=False):
    """--> Calcula o fatorial de um número.
    : param núm: O número a ser calculado.
    : param show: (opcional) Mostrar ou não a conta.

    Returns:
        retorna o valor do Fatorial de um número núm.
    """
    print('-'*20)
    fat = 1
    for c in range(núm, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')        
        fat *= c
    return fat
  
# Programa principal
print(fatorial(5, True))
help(fatorial)
