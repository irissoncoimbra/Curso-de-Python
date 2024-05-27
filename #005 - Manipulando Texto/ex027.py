# Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome:')).title().strip()
nome_split = nome.split()
print('Seu primeiro nome é: {}'.format(nome_split[0]))
print('Seu último nome é: {}'.format(nome_split[-1]))