'''Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''
print('=>'*15, 'DESAFIO 073', '<='*15)
times = ('Flamengo', 'São Paulo', 'Palmeiras', 'Santos', 'Vasco', 'Fluminense', 'Chapecoense', 'River', 'Internacional', 'Botafogo', 'Grêmio', 'Cruzeiro', 'Atlético-PR', 'Atlético-GO', 'Bahia', 'Avaí', 'Coritiba', 'EC Vitória', 'Ponte Preta', 'Sport Recife')
print('-='*20)
print(f'Lista dos times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*20)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'O {times[6]} está na {times.index('Chapecoense')}ª posição')
