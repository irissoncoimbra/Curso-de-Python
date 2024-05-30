# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

#   - Para salários superiores a 1250, calcule um aumento de 10%.
#   - Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite seu salário:'))
if sal >= 1250.00:
    sal_cor = sal + (sal*0.10)
else:
    sal_cor = sal + (sal*0.15)

print('Seu salário corrigido passará a ser: R$ {:.2f}'.format(sal_cor))