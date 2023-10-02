#Aluguel de Carros

valordia = float(input('Insira o valor da diária: '))
diaria = int(input('Insira o número de diárias: '))
valorkm = (int(input('Insira o valor por Km rodado (em centavos): ')))/100
km = int(input('Insira a quantidade de Km rodados: '))
pagamento = (diaria*valordia) + (km*valorkm)

print ('Valor diária: R$ {:.2f}'.format (valordia))
print ('Quantidade de diárias: {}'.format(diaria))
print ('Quantidade de Km rodados {}'.format(km))
print ('Valor por km rodado: R$ {:.2f}'.format(valorkm))
print ('TOTAL A PAGAR: R$ {:.2f}'.format(pagamento))
