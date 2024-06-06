'''Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    - Média abaixo de 3,0: REPROVADO
    - Média entre 3.0 e 6.9: RECUPERAÇÃO
    - Média 7.0 ou superior: APROVADO'''

p1 = float(input('Insira a nota da p1: '))
p2 = float(input('Insira a nota da p2: '))
m = (p1 + p2) / 2
print('Sua média é: {}'.format(m))
if m < 3.0:
    print('Você está REPROVADO')
elif 3.0 <= m <= 6.9:
    print('Você está em RECUPERAÇÃO')
else:
    print('Você está APROVADO')