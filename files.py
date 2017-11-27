miPrimerArchivo = open("lista.txt", "w")
miPrimerArchivo.write("peras\n")
miPrimerArchivo.write("manzanas\n")
miPrimerArchivo.write("Bananas")
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
for linea in miArchivo:
   if(linea.find("manzanas")>-1):
      print("Me gustan las ", linea)
miArchivo.close()
