# Crie um programa que leia o nome de uma pessoa e diga se ela tem ou não Silva no nome.

nome = str(input('Insira seu nome completo:')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))