# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*12)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*12)
r1 = float(input('Insira um seguimento de reta: '))
r2 = float(input('Insira mais um seguimento de reta: '))
r3 = float(input('Insira mais um seguimento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses três seguimentos de reta PODEM FORMAR TRIÂNGULO')
else:
    print('Esses três seguimentos de reta NÃO PODEM FORMAR TRIÂNGULO')