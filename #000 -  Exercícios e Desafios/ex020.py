#Sorteando uma ordem na lista

from random import shuffle
n0 = str(input('Primeiro aluno:'))
n1 = str(input('Segundo aluno:'))
n2 = str(input('Terceiro aluno:'))
n3 = str(input('Quarto aluno:'))
n4 = str(input('Quinto aluno:'))
n5 = str(input('Sexto aluno:'))
n6 = str(input('Sétimo aluno:'))
n7 = str(input('Oitavo aluno:'))
n8 = str(input('Nono aluno:'))
n9 = str(input('Décimo aluno:'))
lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n0]
ordem = shuffle(lista)

print('A ordem escolhida foi:{}'.format(lista))
