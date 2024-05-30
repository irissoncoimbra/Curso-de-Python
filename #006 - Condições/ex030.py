# Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print('{} é um número par'.format(num))
else:
    print('{} é um número ímpar.'.format(num))