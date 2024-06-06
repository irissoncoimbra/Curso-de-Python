'''A confederação brasileira de natação precisa de uma programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JUNIOR
    -Até 20 anos: SÊNIOR
    - ACIMA: PROFISSIONAL'''

from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('Você está na categoria MIRIM')
elif idade <=14:
    print('Você está na categoria INFANTIL')
elif idade <= 19:
    print('Você está na categoria JÚNIOR')
elif idade <=20:
    print('Você está na categoria SÊNIOR')
else:
    print('Você está na categoria PROFISSIONAL')