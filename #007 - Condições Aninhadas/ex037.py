'''   Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

    1) Para binário
    2) Para octal
    3) Para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão: 
      [ 1 ] Converter para BINÁRIO
      [ 2 ] Converter para OCTAL
      [ 3 ] Converter para HEXADECIMAL''')
op = int(input('Sua opção:'))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE!')