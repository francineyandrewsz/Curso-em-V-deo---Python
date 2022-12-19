print('=>'*15, 'DESAFIO 112', '<='*15)

from DESAFIO112.utilidadesCeV import moeda
from DESAFIO112.utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)