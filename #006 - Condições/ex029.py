#Escreva um programa que leia a velocidade de um carro.

#   - Se ele ultrapasar a velocidade de 80km/h, mostre uma mensagem dizendo que ele foi multado.
#   - a multa vai custar R$ 7 por cada Km acima do limite.

velocidade = float(input('Insira a velocidade do carro:'))
multa_final = (velocidade - 80)*7

if velocidade >= 81:
    print ('Sua velocidade era de {} Km/h, portanto, o valor da sua multa é igual a R$ {:.2f}'.format(velocidade, multa_final))
else:
    print('Vocẽ estava dentro do limite permitido para a via! PARABÉNS!')
print('Tenha um bom dia! Dirija com segurança!')