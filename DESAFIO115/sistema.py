'''Crie um pequeno sistema modularizado que permite cadastrar
pessoas pelo seu nome e idade em um arquivo simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e 
listar todas as pessoas cadastradas.'''

from DESAFIO115.lib.interface import *
from DESAFIO115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabecalho('Saindo do sistema...Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
