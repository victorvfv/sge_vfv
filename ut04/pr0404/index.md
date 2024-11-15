## Ejecicios diccionarios

## 1.- Buscar valor en un diccionario
Crea un diccionario de frutas y precios. Permite al usuario ingresar el nombre de una fruta y muestra su precio si existe en el diccionario, o un mensaje de que no está disponible en caso contrario.

```python  

frutas = {
    "manzana": 1.20,
    "banana": 0.50,
    "cereza": 2.00,
    "naranja": 0.80,
    "uva": 3.00
}

frutaBuscada = input("Ingrese el nombre de una fruta: ").lower()

print(f"El precio de "+ frutaBuscada + " es " + str(frutas.get(frutaBuscada,"no esta")) )

``` 

## 2.- Contar elementos en un diccionario
Suponiendo un diccionario con al siguiente estructura, crea un programa que calcule cuántas categorías hay, cuántos productos tiene cada categoría y cuántos productos hay en total.

```python 

productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

numCategorias = len(productos)
print(f"Hay {numCategorias} categorías.")

totalProductos = 0
for categoria, items in productos.items():
    cantidad = len(items)
    totalProductos += cantidad
    print("Categoría "+ categoria + " tiene " + str(cantidad) +" productos.")

print(f"En total hay " + str(totalProductos) + " productos.")

```

## 3.- Contador de frecuencias de palabras
Escribe un programa que tome una frase y use un diccionario para contar la frecuencia de cada palabra.

```python 

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


```  

## 4.- Diccionario de listas
Supón un diccionario donde cada clave es una asignatura y el valor correspondiente una lista de estudiantes matriculados, tal como se muestra en el diccionario de ejemplo. Crea un programa que tenga un menú con tres opciones:

Listar estudiantes matriculados en una asignatura
Matricular un estudiante en una asignatura
Dar de baja un estudiante de una asignatura.

```python 

asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

def listar_estudiantes(asignatura):
    if asignatura in asignaturas:
        print("Estudiantes en "+asignatura + str(asignaturas.get(asignatura)))
    else:
        print("La asignatura no existe.")

def matricular_estudiante(asignatura, estudiante):
    if asignatura in asignaturas:
        if estudiante not in asignaturas[asignatura]:
            asignaturas[asignatura].append(estudiante)
            print(estudiante + "se ha matriculado en" + asignatura)
        else:
            print(estudiante + "ya está matriculado en" + asignatura)
    else:
        print("La asignatura no existe.")

def dar_baja_estudiante(asignatura, estudiante):
    if asignatura in asignaturas:
        if estudiante in asignaturas[asignatura]:
            asignaturas[asignatura].remove(estudiante)
           
        else:
            print(estudiante+ "no está matriculado en" + asignatura)
    else:
        print("La asignatura no existe.")


while True:
    print("Menú de opciones:")
    print("1. Listar estudiantes en una asignatura")
    print("2. Matricular un estudiante en una asignatura")
    print("3. Dar de baja un estudiante de una asignatura")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        listar_estudiantes(input("Ingrese el nombre de la asignatura: "))
    elif opcion == "2":
        matricular_estudiante(input("Ingrese el nombre de la asignatura: "),input("Ingrese el nombre del estudiante: "))
    elif opcion == "3":
        dar_baja_estudiante(input("Ingrese el nombre de la asignatura: "),input("Ingrese el nombre del estudiante: "))
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")

``` 

## 5.- Diccionario invertido
Escribe una función que tome un diccionario y devuelva otro con las claves y valores intercambiados (lo que antes eran valores ahora son claves, y viceversa).


```python 

def invertir(param1):
    param1= {valor: clave for clave, valor in param1.items()}
    print (param1)



invertir({"a": 1, "b": 2, "c": 3})

```

## 6.- Combinar dos diccionarios
Escribe un programa que tome dos diccionarios de productos y precios, y combine los productos comunes sumando sus precios, sin duplicar los elementos únicos.

```python 

def combinarDiccionarios(param1, param2):
    combinado = param1  
    for producto, precio in param2.items():
        if producto in combinado:
            combinado[producto] += precio 
        else:
            combinado[producto] = precio 
    print (combinado)




combinarDiccionarios({"manzana": 1.20, "banana": 0.50, "pera": 1.50}, {"banana": 0.30, "pera": 1.20, "naranja": 0.80})

```