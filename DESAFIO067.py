'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo. '''

print('=>'*15, 'DESAFIO 067', '<='*15)
while True:
    try:
        núm = int(input('Quer ver a tabuada de qual valor?\n'))
        print('-'*30)
        if núm < 0:
            break
        for c in range(1, 11):
            print(f'{núm} x {c} = {núm*c}')
    except:
        print('Operação inválida! Tente novamente.')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        