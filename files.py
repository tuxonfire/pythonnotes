miPrimerArchivo = open("lista.txt", "w")
miPrimerArchivo.write("peras\n")
miPrimerArchivo.write("manzanas")
miPrimerArchivo.close()

print("**Leyendo el archivo: \n")
miArchivo = open("lista.txt")
print(miArchivo.read())
miArchivo.close()