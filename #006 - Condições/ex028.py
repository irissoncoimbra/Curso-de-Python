# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#   -O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
pc = randint(0, 5) #Sorteia o numero entre 0 e 5.
print('-=-' *20)
print('Vou pensar num número entre 0 e 5. Tente advinhar...')
print('-=-' *20)
user = int(input('Chute um número:'))
print('----------- PROCESSANDO -----------')
sleep(3)
if user == pc:
    print('Você acertou! Parabéns!')
else:
    print('Você perdeu! Eu pensei no {}.'.format(pc))