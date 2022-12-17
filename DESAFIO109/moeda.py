'''Modifique as funções que foram criadas no desafio 107 para que elas
aceitem um parâmetro a mais, informando se o valor retornado por elas 
vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

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

