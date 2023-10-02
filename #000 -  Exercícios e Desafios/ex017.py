#Catetos e Hipotenusas

'''co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = (co**2 + ca**2)**(1/2)

print('A Hipotenusa vai medir {:.2f}'.format(hi))'''

'''import math
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = math.hypot(co, ca)

print('A Hipotenusa vai medir {:.2f}'.format(hi))'''

from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)

print('A Hipotenusa vai medir {:.2f}'.format(hi))
