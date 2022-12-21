'''Crie um código em Python que teste se o site 
Pudim está acessível pelo computador usado.'''

print('=>'*15, 'DESAFIO 114', '<='*15)

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento\033[0;0m')
else:
    print('\033[32mConsegui abrir o site Pudim com sucesso!\033[0;0m')
    print(site.read()) # Conteúdo HTML do site
