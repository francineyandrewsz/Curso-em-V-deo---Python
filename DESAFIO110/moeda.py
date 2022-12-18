'''Adicione ao módulo moeda.py criado nos desafios anteriores, 
uma função chamada resumo(), que mostre na tela algumas informações
geradas pelas funções que já temos no módulo criado até aqui.'''

def aumentar(preco=0, taxa=0, formato=False):
    """
    :param preco: passa o valor do preço.
    :param taxa: passa o valor da taxa de desconto.
    :param formato: passa a formatação se for True, senão False.
    :return: retorna o valor da operação
    """
    res = preco + (preco * taxa /100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco=0, taxa_a=10, taxa_r=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade o preço: \t{metade(preco, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(preco, True)}')
    print(f'{taxa_r}% de redução: \t{diminuir(preco, True)}')
    print('-'*30)
    
