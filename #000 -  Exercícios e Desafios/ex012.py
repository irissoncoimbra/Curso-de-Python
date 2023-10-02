#Calculando descontos

preco = float(input('Digite o preço do produto: R$ '))
desconto = float(input('Digite quanto de desconto a ser aplicado (%): '))
precodesconto = preco - (preco * (desconto/100))

print('O preço do produto é igual a R${} e com desconto de {}% o preço final é igual a R$ {}' .format(preco, desconto, precodesconto))