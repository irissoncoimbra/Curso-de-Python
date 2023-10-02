#import math
#num = int(input('digite um número: '))
#raiz = math.sqrt(num)

#print('A raiz de {} é igual a {}. Arredondando pra cima fica igual a {:.2f}. Arredondando pra baixo: {:.2f}.'.format(num, raiz, math.ceil(raiz), math.floor(raiz)))

from math import sqrt
num = int(input('digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}.'.format(num, raiz))

#Ex0016 até 
