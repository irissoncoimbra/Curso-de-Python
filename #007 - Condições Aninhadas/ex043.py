'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    - Abaixo de 18.5: Abaixo do peso
    - Entre 18.5 e 25: Peso ideal
    - 25 até 30: Sobrepeso
    - 30 até 40: Obesidade
    - Acima de 40: Obesidade mórbida'''

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em METROS (ex.: 1.78)'))
imc = peso / (altura**2)
print ('''
       Sua altura é: {:.2f}
       Seu peso é: {:.2f}
       Seu imc é: {:.2f}
       '''.format(peso, altura, imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL')
elif 18.5 <= imc <= 25:
    print('Você está no PESO IDEAL')
elif 25 < imc <= 30:
    print('Você está com SOBREPESO')
elif 30 < imc <= 40:
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA')