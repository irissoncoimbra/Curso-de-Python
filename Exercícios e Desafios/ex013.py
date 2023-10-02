#Reajuste de salário
salario = float(input('Digite o salário atual do contribuinte:'))
reajuste = float(input('Digite o valor do reajuste:'))
salarioreajustado = salario + (salario*(reajuste/100))

print ('O salário atual do contribuinte é igual a R$ {:.2f}, com o reajuste de {:.0f}%, o salário passará a ser de R$ {:.2f}.' .format(salario, reajuste, salarioreajustado))