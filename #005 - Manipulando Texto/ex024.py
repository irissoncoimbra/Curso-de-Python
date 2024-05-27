# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra Santo.

city = str(input('Insira o nome de uma cidade:')).strip()
print(city[:5].upper() == 'SANTO')
