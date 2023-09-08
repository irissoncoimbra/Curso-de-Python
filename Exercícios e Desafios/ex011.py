#Quanto de tinta precisa ter para pintar uma parede

largura = float(input('Digite a Largura da sua parede (m): '))
altura = float(input('Digite a altura da sua parede(m): '))
area = largura*altura
tinta = area/2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²' .format(largura, altura, area))
print('Para pintar sua parede, serão necessários {} litros de tinta' .format(tinta))