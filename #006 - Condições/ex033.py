# Faça um programa que leia 3 números e diga qual é o maior e qual é menor.

num1 = int(input('Digite um número:'))
num2 = int(input('Digite mais um número:'))
num3 = int(input('Digite mais um número:'))

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

#Verificando quem é maior:
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O número de menor valor é o: {}'.format(menor))
            #print('O número do meio é o: {}'.format(meio))
print('O número de maior valor é: {}'.format(maior))