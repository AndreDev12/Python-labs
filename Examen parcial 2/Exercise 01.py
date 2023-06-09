days_str = input('¿Cuántos días desea alojarse?')
days = int(days_str)

# print(days, 'días')

# Solo ingresar categoría 3 ó 5
category_str = input('¿Qué categoría elige?')
category = int(category_str)
# print(category, 'estrellas')

if(days > 10):
   if(category == 3):
     costo = days * 60
   if(category == 5):
     costo = days * 120
if(7<=days and days <=10):
   if(category == 3):
     costo = days * 80
   if(category == 5):
     costo = days * 130
if(4<=days and days <=6):
   if(category == 3):
     costo = days * 90
   if(category == 5):
     costo = days * 140
if(1<=days and days <=3):
   if(category == 3):
     costo = days * 100
   if(category == 5):
     costo = days * 160         

print('El pago total es', costo)

# Ingresar si o no
breakfast = input('¿Desea tomar desayuno?')

if(breakfast == 'si'):
 costo_total = costo + 10 * days
else:
  costo_total = costo

print('El pago total es', costo_total)