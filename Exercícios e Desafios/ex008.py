#Conversor de medidas

med = float(input('Insira a sua medida em metros:'))

mm = med*1000
cm = med*100
dm = med*10
m = med*1
dam = med*0.1
hm = med*0.01
km = med*0.001

print ('As medidas convertidas são:')

print("Milimetros (mm): {}.\nCentímetros (cm): {}.\nDecímetros (cm): {}.\nDecâmetros (dam): {}.\nHectometro (hm): {}\nKilometro (km): {}\n" .format(mm, cm, dm, dam, hm, km))


