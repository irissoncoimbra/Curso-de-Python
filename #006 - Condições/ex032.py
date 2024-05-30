# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 
#   - NOTA: anos bissextos são anos múltiplos de 4, exceto multiplos de 100 que não são múltiplos de 400.

ano = int(input('Digite o ano pra saber se ele foi ou será bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))