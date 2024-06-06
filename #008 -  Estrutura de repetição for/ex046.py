'''Faça um programa qie mostre na tela uma contagem regressiva para o estouro de fogos, indo de 10 até o 0, com pausa de 1 segundo entre eles'''

from time import sleep
for cont in range (10, -1, -1):
    print(cont)
    sleep(1)
print('BUM! BUM! POW!')