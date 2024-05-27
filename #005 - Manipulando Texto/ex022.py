#Crie um programa que leia o nome completo de uma pessoa e mostre:

#   - O nome com todas as letras maiúsculas
#   - O nome com todas as letras minúsculas
#   - Quantas letras ao todo (sem considerar os espaços)
#   - Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo:')).strip()
primeiro_nome = nome.split()

print('O seu nome é: {}'.format(nome.title()))
print('Analisando seu texto...')
print('O seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas:{}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome[0], len(primeiro_nome[0])))