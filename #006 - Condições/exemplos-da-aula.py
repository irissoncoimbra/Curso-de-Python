#nome = str(input('Qual é seu nome?:'))

#if nome == "Irisson":
  #  print('Que nome bonito!')
#else:
 #   print('Seu nome é uma merda!')
#print("Bom dia, {}".format(nome))

n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1+n2)/2
print('A sua média é: {:.1f}'.format(m))
if 3.0 < m >=6.0:
  print ('Vocẽ está aprovado!')
if 3.0 < m < 6.0:
  print ('Você está em recuperação! Mas não se desanime, continue estudando!')
if m < 3.0:
  print ('Você está reprovado sem a possibilidade de recuperação! Boa sorte no próximo semestre!')