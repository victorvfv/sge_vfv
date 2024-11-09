frase = input("Ingrese una frase: ")
palabras = frase.split()

frecuenciaPalabras = {}


for palabra in palabras:
    if palabra in frecuenciaPalabras:
        frecuenciaPalabras[palabra] += 1
    else:
        frecuenciaPalabras[palabra] = 1


for palabra, frecuencia in frecuenciaPalabras.items():
    print("La palabra " + palabra + " aparece " + str(frecuencia) + " veces.")