'''
    Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela uma mensagem:
        1) O primeiro valor é maior
        2) O segundo valor é maior
        3)Não existe valor maior, os dois são iguais.
'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número:'))
if n1 > n2:
    print('O primeiro valor({}) é maior que o segundo valor({})'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor ({}) é maior que o primeiro valor ({})'.format(n2, n1))
else:
    print('Os valores são iguais.')