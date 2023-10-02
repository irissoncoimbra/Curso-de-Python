#Conversor de temperaturas

celsius = float(input("Digite a temperatura em Celsius:"))
farenheit = ((celsius*9)/5)+32
kelvin = celsius+273

print ("Celsius: {} ºC".format(celsius))
print ('Farenheit: {} ºF'.format(farenheit))
print ('Kelvin: {} K'.format(kelvin))