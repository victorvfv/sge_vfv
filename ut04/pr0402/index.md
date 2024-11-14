##  Ejercicios de cadenas
## 1. Contar vocales y consonantes
Escribe una función que reciba una cadena y cuente cuántas vocales y consonantes contiene.

´´´Python 

def contadorVocalesYConsonates(param1):
    v=param1.count("a")
    v+=param1.count("e")
    v+=param1.count("i")
    v+=param1.count("o")
    v+=param1.count("u")
    
    c=len(param1.replace(" ",""))
    c=c-v
    print("Hay "+ str(c) +" consonantes y hay " + str(v) + " Vocales") 
n=contadorVocalesYConsonates("hola hola")

´´´Python 

## 2. Invertir una cadena
Crea un programa que invierta una cadena.

´´´Python 

def invertir(param1):
    n=param1.split(" ")
    n.reverse()
    salida=" ".join(n)
    print(salida)

invertir(input())

´´´Python 

## 3. Verificar palíndromo
Escribe un programa que verifique si una cadena es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).

´´´Python 

def palindromo(param1):
    c=len(param1)
    n=[]
    for num in range (c):
        n.append(param1[num])
    
    n.reverse()
    b="".join(n)
    if (b==param1):
        print("es un palindromo")
    else:
        print("no es un palindromo")

palindromo("ana")

´´´Python 

## 4. Contar palabras
Crea una función que cuente cuántas palabras hay en una cadena, suponiendo que las palabras están separadas por espacios.

´´´Python 

def contador(param1):
    
    n=param1.split(" ")
    
    b=int(0)
    for elem in n:
        b=b+1
    print(b)

contador("hola caracola tonta")

´´´Python 

## 5. Eliminar caracteres repetidos
Escribe una función que elimine los caracteres duplicados en una cadena, manteniendo solo la primera aparición de cada uno.

´´´Python 

def removeChar(param1):
    list=[]
    iter=[]
    cadena=param1
    for char in cadena:
        list.append(char)
        iter.append(char)

    list.reverse()

    for char in iter: 
        if list.count(char)>=2:
            list.remove(char)
        
    list.reverse()

    salida="".join(list)
    print(salida)

removeChar(input())


´´´Python 

## 6. Mayúsculas y minúsculas
Escribe un programa que convierta las letras minúsculas de una cadena en mayúsculas y viceversa.

´´´Python 

def mayusminus(param1):
    print(param1.swapcase())

mayusminus(input())

´´´Python 