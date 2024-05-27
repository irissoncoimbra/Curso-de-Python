# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#num = str(input('Digite um numero de 0 a 9999:'))

#print('A casa da milhar é: {}'.format(num[0]))
#print('A casa da centena é: {}'.format(num[1]))
#print('A casa da dezena é: {}'.format(num[2]))
#print('A casa da unidade é: {}'.format(num[3])) ---> a forma que eu fiz inicialmente

num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))

print('Unidade: {}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))