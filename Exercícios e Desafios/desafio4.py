#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

var=input('Insira um valor:')

print('É númerico?', var.isnumeric())
print('É alfabético?', var.isalpha())
print('É decimal?', var.isdecimal())
print('É alfanumérico?', var.isalnum())
print('Está em letra maiúscula?', var.isupper())
print('Está em letra minuscula?', var.islower())
print('É printável?', var.isprintable())