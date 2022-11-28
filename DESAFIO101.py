'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''
print('=>'*15, 'DESAFIO 101', '<='*15)

def voto(ano):
    from datetime import date
    print('-'*20)
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: seu Voto é NEGADO.'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: seu voto é OPCIONAL.'
    else:
        return f'Com {idade} anos: seu voto é OBRIGATÓRIO.'


# Programa principal
nasc = int(input('Em que ano você nasceu?\n'))
print(voto(nasc))
