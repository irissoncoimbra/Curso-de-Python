# Desenvolva um programa que pergunte a distância em Km. calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens até 200 km e 0,45 para viagens mais longas.

km = float(input('Digite a distância da sua viagem em Km: '))
if km <= 200:
    print('A sua viagem custará R$ {:.2f}'.format(km*0.5))
    '''preço = km * 0.50'''
else:
    print('A sua viagem custará R$ {:.2f}'.format(km*0.45))
    '''preço = km * 0.45
    print(preço) ---> Seria uma outra maneira de resolver o exercício
        - Que foi uma atribuição de variável dentro das estruturas condcionais.'''