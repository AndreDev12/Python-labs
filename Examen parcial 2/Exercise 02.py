anios_str = input('¿Cuántos años tiene?')
anios = int(anios_str)

adivinanzas_str = input('¿Cuántas adivinanzas acertó?')
adivinanzas = int(adivinanzas_str)

# print(anios, 'años')
# print(adivinanzas)

if(17 < anios):
   if(adivinanzas < 3):
     monto_inicial = 30
   else:
     monto_inicial = 50
else:
   if(adivinanzas < 3):
     monto_inicial = 50
   else:
     monto_inicial = 80

monto_total_ganador = monto_inicial + 5 * anios + 2 * adivinanzas
print(monto_total_ganador)