'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
a possibilidade da digitação de número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funionalidade.'''

print('=>'*15, 'DESAFIO 112', '<='*15)
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digiter esse número.\033[m')
            return 0
        else:
            return n
            
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


valor1 = leiaInt('Digite um valor Inteiro: ')
valor2 = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {valor1} e o real foi {valor2}')
