'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição e pagamento:
    - à vista dinheiro/cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2x no cartão: preço normal
    - 3x ou mais: 20% de juros'''

prod = float(input('Digite o valor do produto:'))
print('''ESCOLHA UMA FORMA DE PAGAMENTO:
      [1] Á VISTA no DINHEIRO
      [2] Á VISTA no CARTÃO
      [3] EM ATÉ 2X no cartão
      [4] EM 3X OU MAIS''')
op = int(input('Sua forma de pagamento: '))
if op == 1:
    print('Total a pagar: R$ {:.2f}'.format(prod - (prod * 0.1)))
elif op == 2:
    print('Total a pagar: R$ {:.2f}'.format(prod - (prod * 0.05)))
elif op == 3:
    print('Total a pagar: R$ {:.2f} em 2x de R$ {:.2f}'.format(prod, (prod / 2)))
elif op == 4:
    parcelas = int(input('Em quantas vezes deseja pagar?: '))
    print('Total a pagar: R$ {:.2f} em {}x de {:.2f}'.format((prod + (prod * 0.2)), parcelas, ((prod + prod * 0.2) / parcelas)))