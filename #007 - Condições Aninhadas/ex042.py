'''Refaça o exercício 35 dizendo dessa vez se os seguimentos de reta formam um triângulo, e se sim, se ele é equilátero, sosceles ou escaleno

    - Equilatero: todos os lados iguais
    - Isósceles: dois lados iguais
    - Escaleno: todos os lados diferentes'''

r1 = float(input('Insira um segmento de reta: '))
r2 = float(input('Insira mais um segmento de reta: '))
r3 = float(input('Insira mais um segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos de reta acima PODEM FORMAR TRIÂNGULO ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos de reta acima NÃO PODEM FORMAR TRIÂNGULO!')