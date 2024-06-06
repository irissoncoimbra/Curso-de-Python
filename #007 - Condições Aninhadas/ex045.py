'''Crie um programa que faça o computador que faça o computador jogar Jokenpo com você'''

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint (0,2)
print('O computador jogou: {}'.format(itens[pc]))