#   Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#   Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa em R$: '))
salario_comprador = float(input('Digite o seu salário em R$: '))
pagamento_ano = int(input('Digite em quantos anos você pagará o financiamento: '))
qtd_meses = pagamento_ano*12
parcela = valor_casa / qtd_meses

if salario_comprador * 0.30 < parcela:
    print('FINANCIAMENTO NÃO APROVADO')
else:
    print('FINANCIAMENTO APROVADO')
    print('Suas parcelas mensais serão de R$ {:.2f}'.format(parcela))