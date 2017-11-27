miPrimerArchivo = open("lista.txt", "w")
miPrimerArchivo.write("peras\n")
miPrimerArchivo.write("manzanas\n")
miPrimerArchivo.write("Bananas\n")
miPrimerArchivo.close()

print("**Leyendo el archivo: \n")
miArchivo = open("lista.txt")
print(miArchivo.read())
miArchivo.close()

print("\n**Linea por linea.\n")
miArchivo = open("lista.txt")
for linea in miArchivo:
    print(linea)
miArchivo.close()

print("\n Validando contenido")
miArchivo = open("lista.txt")
for lista in miArchivo:
   if(lista.find("manzanas")>-1):
      print("Me gustan las ", lista)
   else:
     print(lista)
miArchivo.close()

print("\nUsando Readline\n")
miArchivo = open("lista.txt")
print(miArchivo.readline())
print(miArchivo.readline())
print(miArchivo.readline())
miArchivo.close()

print("\nUsando ReadlineS\n")
miArchivo = open("lista.txt")
print(miArchivo.readlines())
miArchivo.close()   

print("\nUsando Read\n")
miArchivo = open("lista.txt")
print(miArchivo.read(7))
miArchivo.close()

#WITH

print("\nUsando With: \n")
with open("lista.txt") as miArchivo:
    print(miArchivo.read(7))


