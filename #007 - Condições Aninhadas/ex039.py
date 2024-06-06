'''Faça um prgrama que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - Se ele ainda pode se alistar no serviço militar
    - Se é a hora de se alistar
    - Se já passou do tempo de alistamento.
    
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''

from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
sub_ano = ano_atual - ano_nascimento
idade_sub = (ano_atual - ano_nascimento) - 18
if sub_ano == 18:
    print('Você deve se alistar às forcas armadas esse ano')
elif sub_ano > 18:
    print('Você já passou do período de alistamento há {} anos.'.format(idade_sub))