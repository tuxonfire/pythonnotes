ahorros = 50
#ahorros = input("¿Cuánto tienes ahorrado?")
#print("Tienes ahorrado , ", ahorros)
if ahorros > 300:
    print('comprar xbox')
elif ahorros > 100:
    print('tienes ahorrado %s , Ya casi' %ahorros )
elif ahorros > 200:
    print('Ya puedes comprar el xbox')
elif ahorros == 100:
    print("solo tenemos %s" %ahorros )
    print("sigue ahorrando más para el xbox")
else:
    print('Tenemos otra cantidad de dinero')
