# my_notes
archivo = open("my_notes.txt", "w")
archivo.write("1. Revisar apuntes de clase.\n")
archivo.write("2. Practicar ejercicios de Python.\n")
archivo.write("3. Preparar la presentación del proyecto.\n")
archivo.close()

# Leer el archivo línea por línea usando readline()
archivo = open("my_notes.txt", "r")

linea = archivo.readline()
while linea:
    print(linea.strip())  # Mostramos la línea sin salto de línea extra
    linea = archivo.readline()

archivo.close()
