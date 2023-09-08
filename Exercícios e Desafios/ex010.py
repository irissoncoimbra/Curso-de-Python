#Conversor de Moeda

real = float(input('Quanto você quer trocar? R$ '))
dolar = real / 4.99

print('Com R$ {:.2f}, você pode comprar US$ {:.2f}' .format(real, dolar))
