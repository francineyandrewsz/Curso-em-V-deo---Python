''' Dentro do pacote utilidadesCeV que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função imputa(), mas com uma
validação de dados para aceitar apenas valores que seja monetários.'''

def aumentar(preco=0, taxa=0, formato=False):
    """
    --> Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a sáida formatada ou não?
    :return: o valor reajustado com ou sem formato.
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
    
